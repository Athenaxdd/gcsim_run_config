import subprocess
import csv
import re
import json
import logging

# Set up logging
csv_filename = input('Enter the name of the output CSV file: ')

logging.basicConfig(filename=f'{csv_filename}_log.txt', level=logging.INFO, format='%(asctime)s %(message)s')


logging.info('Script started. Output CSV file: %s', csv_filename)

with open('batch.txt', 'r') as file:
    for line in file:
        command = line.strip()
        logging.info('Processing command: %s', command)
        batch_name_match = re.search(r'"(.*).txt"', command)

        if batch_name_match is not None:
            batch_name = batch_name_match.group(1)
            logging.info('Batch name: %s', batch_name)

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, _ = process.communicate()
        logging.info('Command output: %s', output.decode(encoding='utf-8', errors="ignore"))

        lines = output.decode(encoding='utf-8', errors="ignore").split('\n')

        average_damage = duration = dps = min_dps = max_dps = std_dps = None

        for line in lines:
            pattern = r'Average ([\d.]+) damage over ([\d.]+) seconds, resulting in ([\d]+) dps \(min: ([\d.]+) max: ([\d.]+) std: ([\d.]+)\)'
            match = re.search(pattern, line)
            if match:
                average_damage = match.group(1)
                duration = match.group(2)
                dps = match.group(3)
                min_dps = match.group(4)
                max_dps = match.group(5)
                std_dps = match.group(6)
                logging.info('Parsed DPS info: Avg Damage=%s, Duration=%s, DPS=%s, Min DPS=%s, Max DPS=%s, Std DPS=%s',
                                average_damage, duration, dps, min_dps, max_dps, std_dps)
        
        json_filename = f'./viewer_json/{batch_name}.json'
        character_details = []
        try:
            with open(json_filename, 'r') as json_file:
                data = json.load(json_file)
                logging.info('Loaded JSON data from %s', json_filename)
                # Extract character DPS details
                for i in range(len(data['character_details'])):
                    name = data['character_details'][i]['name']
                    stats = data['statistics']['character_dps'][i]
                    character_details.append({
                        "name": name,
                        "min": stats["min"],
                        "max": stats["max"],
                        "mean": stats["mean"],
                        "sd": stats["sd"]
                    })
                    logging.info('Character details: %s, Min DPS=%s, Max DPS=%s, Mean DPS=%s, Std DPS=%s',
                                    name, stats["min"], stats["max"], stats["mean"], stats["sd"])
        except FileNotFoundError:
            logging.warning('JSON file not found: %s', json_filename)
            pass
        except json.JSONDecodeError as e:
            logging.error('Error decoding JSON from file %s: %s', json_filename, str(e))
            pass

        row = [batch_name, 'Total Avg Damage:', average_damage, 'DPS:', dps, 'Min DPS:', min_dps, 'Max DPS:', max_dps, 'Std DPS:', std_dps]

        for character in character_details:
            row.extend([character["name"], "Min DPS:", character["min"], "Max DPS:", character["max"], "Mean DPS:", character["mean"], "Std DPS:", character["sd"]])

        with open(f'{csv_filename}.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)
            logging.info('Written row to CSV: %s', row)

logging.info('Script finished.')
print("Batch run Complete!")

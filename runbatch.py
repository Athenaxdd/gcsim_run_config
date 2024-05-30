import subprocess
import csv
import re
import json

csv_filename = input('Enter the name of the output CSV file: ')

# Open the text file
with open('batch.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Strip the newline character at the end of the line
        command = line.strip()

        # Extract the name of the batch file
        batch_name_match = re.search(r'"(.*).txt"', command)
        if batch_name_match is not None:
            batch_name = batch_name_match.group(1)

        # Execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Capture the output
        output, _ = process.communicate()

        # Decode the output and split it into lines
        lines = output.decode(encoding='utf-8', errors="ignore").split('\n')

        # Initialize the variables for DPS information
        average_damage = duration = dps = min_dps = max_dps = std_dps = None

        # Check each line for the DPS information
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
        
        # Check if JSON output exists and process it
        json_filename = f'./viewer_json/{batch_name}.json'
        character_details = []
        try:
            with open(json_filename, 'r') as json_file:
                data = json.load(json_file)
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
        except FileNotFoundError:
            pass

        # Prepare a single row of data for the CSV file
        row = [batch_name, 'Total Avg Damage:', average_damage, 'DPS:', dps, 'Min DPS:', min_dps, 'Max DPS:', max_dps, 'Std DPS:', std_dps]

        for character in character_details:
            row.extend([character["name"], "Min DPS:", character["min"], "Max DPS:", character["max"], "Mean DPS:", character["mean"], "Std DPS:", character["sd"]])

        # Write the information to a CSV file
        with open(f'{csv_filename}.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)

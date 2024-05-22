
import subprocess
import csv
import re

csv_filename = input('Enter the name of the output CSV file: ')
# Open the text file
with open('batch.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Strip the newline character at the end of the line
        command = line.strip()

        # Extract the name of the batch file
        batch_name = re.search(r'"(.*).txt"', command)
        if batch_name is not None:
            batch_name = batch_name.group(1)

        # Execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Capture the output
        output, _ = process.communicate()

        # Decode the output and split it into lines
        lines = output.decode(encoding='utf-8', errors="ignore").split('\n')

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

                # Write the information to a CSV file
                with open(f'{csv_filename}.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([batch_name, 'total avg dps:', average_damage, 'DPS:', dps, 'Min DPS:', min_dps, 'Max DPS:', max_dps, 'Std DPS:', std_dps])


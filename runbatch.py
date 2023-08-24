import csv
import os
import re

# Take the character name as input from the keyboard
character_name = input("Enter character name: ")

with open('batch.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        # Extract the character name from the command line
        match = re.search(r'"(\w+).txt"', line)
        if match:
            cmd_character_name = match.group(1)

            # Run the command
            stream = os.popen(line)
            cmd_output = stream.read()

            # Extract the total average DPS information for the specified character
            pattern = character_name + r' total avg dps: ([\d.]+)'
            match = re.search(pattern, cmd_output)
            if match:
                avg_dps = match.group(1)

                # Extract the average damage, duration, and DPS information
                pattern = r'Average ([\d.]+) damage over ([\d.]+) seconds, resulting in ([\d]+) dps'
                match = re.search(pattern, cmd_output)
                if match:
                    average_damage = match.group(1)
                    duration = match.group(2)
                    dps = match.group(3)

                    # Write the information to a CSV file
                    with open('output.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([character_name + ' total avg dps:', avg_dps, 'DPS:', dps, cmd_character_name])

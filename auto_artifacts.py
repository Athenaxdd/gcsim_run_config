import re
import os

script_filename = input("Enter the name of the script file (include the .txt): ")
with open(script_filename, 'r') as f:
    script = f.read()

with open('./artifacts/artifacts.txt', 'r') as f:
    sets = f.read().splitlines()

character_input = input("Enter a character name: ")
if character_input not in script.split():
    print(f"{character_input} not found in script")
else:
    os.makedirs('output', exist_ok=True)
    for set_line in sets:
        set_parts = set_line.split()
        set_name = set_parts[0]
        set_count = set_parts[1] if len(set_parts) > 1 else 4
        lines = script.split('\n')
        count = 0
        for i, line in enumerate(lines):
            if line.startswith(f'{character_input} add set'):
                count += 1
                if count > 1:
                    lines[i] = None
                else:
                    lines[i] = re.sub(r'set=".+?"', f'set="{set_name}"', line)
                    if set_count is not None:
                        lines[i] = re.sub(r'count=\d+', f'count={set_count}', lines[i])
        new_script = '\n'.join([line for line in lines if line is not None])
        with open(f'output/{set_name}.txt', 'w') as f:
            f.write(new_script)
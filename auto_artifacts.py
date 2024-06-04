import re
import os

script_filename = input("Enter the name of the script file (include the .txt): ")
with open(script_filename, 'r') as f:
    script = f.read()

set_num = input("Type 4pc or 2pc depending on what you want: ")
if set_num not in ['4pc', '2pc']:
    print(f"{set_num} not a valid input")
    exit()

arti_txt = input("Enter the name of the artifacts file: ")
if f"{arti_txt}.txt" not in os.listdir('artifacts'):
    print(f"{arti_txt}.txt not found in current directory")
    exit()
else:
    with open(f'./artifacts/{arti_txt}.txt', 'r') as f:
        sets = f.read().splitlines()

character_input = input("Enter a character name: ")
if character_input not in script.split():
    print(f"{character_input} not found in script")
elif set_num == '4pc':
    os.makedirs(f'{character_input} artifacts 4pc output', exist_ok=True)
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
        with open(f'{character_input} artifacts output/{set_name}.txt', 'w') as f:
            f.write(new_script)
elif set_num == '2pc':
    os.makedirs(f'{character_input} artifacts 2pc output', exist_ok=True)

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i].split()[0]
            set2 = sets[j].split()[0]
            lines = script.split('\n')
            new_lines = []
            insertion_index = None
            
            for index, line in enumerate(lines):
                if line.startswith(f'{character_input} add set'):
                    if insertion_index is None:
                        insertion_index = index  # Remember the first index where set lines were found
                else:
                    new_lines.append(line)
            
            if insertion_index is not None:
                new_lines.insert(insertion_index, f'{character_input} add set="{set2}" count=2;')
                new_lines.insert(insertion_index, f'{character_input} add set="{set1}" count=2;')
            
            new_script = '\n'.join(new_lines)
            
            output_filename = f'{character_input} artifacts 2pc output/{set1}_{set2}.txt'
            with open(output_filename, 'w') as f:
                f.write(new_script)
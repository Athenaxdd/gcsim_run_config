import re
import os

script_filename = input("Enter the name of the script file (include the .txt): ")
with open(script_filename, 'r') as f:
    script = f.read()

weapon_input = input("Enter a weapon type: ")
if f"{weapon_input}.txt" not in os.listdir('weapons'):
    print(f"{weapon_input}.txt not found in current directory")
else:
    with open(f'./weapons/{weapon_input}.txt', 'r') as f:
        weapons = f.read().splitlines()

    character_input = input("Enter a character name: ")
    if character_input not in script.split():
        print(f"{character_input} not found in script")
    else:
        os.makedirs(f'{character_input} {weapon_input} output', exist_ok=True)
        for weapon in weapons:
            lines = script.split('\n')
            for i, line in enumerate(lines):
                if line.startswith(f'{character_input} add weapon'):
                    lines[i] = re.sub(r'weapon=".+?"', f'weapon="{weapon}"', line)
            new_script = '\n'.join(lines)
            with open(f'{character_input} {weapon_input} output/{weapon}.txt', 'w') as f:
                f.write(new_script)

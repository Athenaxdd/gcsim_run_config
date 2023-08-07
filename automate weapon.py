import re
import os

script_filename = input("Enter the name of the script file (include the .txt): ")
with open(script_filename, 'r') as f:
    script = f.read()

input_word = input("Enter a weapon type: ")
if f"{input_word}.txt" not in os.listdir():
    print(f"{input_word}.txt not found in current directory")
else:
    with open(f'{input_word}.txt', 'r') as f:
        weapons = f.read().splitlines()

    character_input = input("Enter a character name: ")
    if character_input not in script.split():
        print(f"{character_input} not found in script")
    else:
        os.makedirs('output', exist_ok=True)
        for weapon in weapons:
            lines = script.split('\n')
            for i, line in enumerate(lines):
                if line.startswith(f'{character_input} add weapon'):
                    lines[i] = re.sub(r'weapon=".+?"', f'weapon="{weapon}"', line)
            new_script = '\n'.join(lines)
            with open(f'output/{weapon}.txt', 'w') as f:
                f.write(new_script)
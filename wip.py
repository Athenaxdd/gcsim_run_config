import subprocess

with open('commands.txt', 'r') as f:
    commands = f.read().splitlines()

for command in commands:
    subprocess.run(command, shell=True)
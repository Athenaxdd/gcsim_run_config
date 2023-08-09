import os

with open('batch.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        os.system(line)
input_filename = input('Enter the name of the weapon type to generate batch: ')
output_filename = input('Enter the name of the output file: ')

with open(f'./weapons/{input_filename}.txt', 'r') as f:
    words = f.read().split()

with open(f'{output_filename}_output.txt', 'w') as f:
    for word in words:
        f.write('.\\run_optimizer_full.bat "{}.txt"\n'.format(word))

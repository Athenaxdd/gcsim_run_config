input_filename = input('Enter the name of the input file: ')
output_filename = input('Enter the name of the output file: ')

with open(input_filename, 'r') as f:
    words = f.read().split()

with open(f'{output_filename}_output.txt', 'w') as f:
    for word in words:
        f.write('.\\run_optimizer_full.bat "{}.txt"\n'.format(word))

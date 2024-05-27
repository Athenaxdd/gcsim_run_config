config_type = input('Enter the type of config you want to generate batch for (artifacts or weapons): ')
if config_type == 'artifacts':
    input_filename = input('Enter the name of the artifacts file to generate batch: ')
    output_filename = input('Enter the name of the output file: ')
    with open(f'./artifacts/{input_filename}.txt', 'r') as f:
        words = f.read().split()
    with open(f'{output_filename}_output.txt', 'w') as f:
        for word in words:
            f.write('.\\run_optimizer_full.bat "{}.txt"\n'.format(word))
elif config_type == 'weapons':
    input_filename = input('Enter the name of the weapon type to generate batch: ')
    output_filename = input('Enter the name of the output file: ')
    with open(f'./weapons/{input_filename}.txt', 'r') as f:
        words = f.read().split()
    with open(f'{output_filename}_output.txt', 'w') as f:
        for word in words:
            f.write('.\\run_optimizer_full.bat "{}.txt"\n'.format(word))
# input_filename = input('Enter the name of the weapon type to generate batch: ')
# output_filename = input('Enter the name of the output file: ')

# with open(f'./weapons/{input_filename}.txt', 'r') as f:
#     words = f.read().split()

# with open(f'{output_filename}_output.txt', 'w') as f:
#     for word in words:
#         f.write('.\\run_optimizer_full.bat "{}.txt"\n'.format(word))

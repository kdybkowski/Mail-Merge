from pathlib import Path

# Constant
PLACEHOLDER = '[name]'
YOURNAME = 'XYZ'

# Nested directory structure
input_path_letters = Path(r'Input\Letters')
input_path_names = Path(r'Input\Names')
output_path_ready = Path(r'Output\ReadyToSend')

# Create nested directories
try:
    input_path_letters.mkdir(parents=True, exist_ok=True)
except FileExistsError:
    print(f"Directory '{input_path_letters}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{input_path_letters}'.")
except Exception as e:
    print(f'An error occurred: {e}')

try:
    input_path_names.mkdir(parents=True, exist_ok=True, mode=0o666)
except FileExistsError:
    print(f"Directory '{input_path_names}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{input_path_names}'.")
except Exception as e:
    print(f'An error occurred: {e}')

try:
    output_path_ready.mkdir(parents=True, exist_ok=True)
except FileExistsError:
    print(f"Directory '{output_path_ready}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{output_path_ready}'.")
except Exception as e:
    print(f'An error occurred: {e}')

try:
    with open('./Input/Names/invited_names.txt') as names_file:
        names = names_file.readlines()

    with open('./Input/Letters/starting_letter.txt') as letter_file:
        letter_contents = letter_file.read()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
            with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as completed_letter:
                completed_letter.write(new_letter)
except FileNotFoundError:
    with open(r'./Input/Names/invited_names.txt', 'w') as create_names_file:
        create_names_file.write('')
    with open('./Input/Letters/starting_letter.txt', 'w') as create_letter_file:
        create_letter_file.write('''Dear [name],

You are invited to my birthday this Tuesday.

Hope you can make it!

'''+f'{YOURNAME}')

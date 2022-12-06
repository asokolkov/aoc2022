def read_file(file_directory):
    with open(f'../{file_directory}/input.txt', 'r') as f:
        return f.readlines()

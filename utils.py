def read_file_content(file_path):
    """
    Reads the content of a file and returns it as a string.

    :param file_path: The path to the file.
    :return: The content of the file as a string.
    :raises: IOError if the file cannot be read.
    """
    try:
        with open('input/' + file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
    

def read_file_content_raw(file_path):
    """
    Reads the content of a file and returns it as a string.

    :param file_path: The path to the file.
    :return: The content of the file as a string.
    :raises: IOError if the file cannot be read.
    """
    try:
        with open('input/' + file_path, 'r', encoding='utf-8') as file:
            return ''.join(file.readlines())
    except IOError as e:
        print(f"Error reading file: {e}")
        return None
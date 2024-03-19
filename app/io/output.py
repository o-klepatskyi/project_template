def print_to_console(text: str):
    """
    Prints the given text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)

def write_to_file(text: str, filename: str):
    """
    Writes the given text to a file.

    Args:
        text (str): The text to be written.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as file:
        file.write(text)

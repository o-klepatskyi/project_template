import pandas as pd
def get_user_input(prompt: str = "Enter your text: ") -> str:
    """
    Prompt the user for input and return the entered text.

    Args:
        prompt (str, optional): The prompt to display to the user. Defaults to "Enter your text: ".

    Returns:
        str: The text entered by the user.
    """
    return input(prompt)


def read_file(filename: str) -> str:
    """
    Read the contents of a file and return it as a string.

    Args:
        filename (str): The path to the file.

    Returns:
        str: The contents of the file as a string.
    """
    with open(filename, 'r') as file:
        return file.read()


def read_file_with_pandas(filename: str) -> str:
    """
    Read the contents of a file using pandas and return it as a string.

    Args:
        filename (str): The path to the file.

    Returns:
        str: The contents of the file as a string.
    """
    data = pd.read_csv(filename)
    return data.to_string(index=False)

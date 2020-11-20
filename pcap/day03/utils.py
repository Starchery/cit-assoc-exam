class EmptyFile(Exception):
    """
    This will be raised if the CSV passed in is empty

    An EmptyFile is a "special case" of an Exception.
    """

    def __init__(self, message):
        super().__init__(message)


def clean_file(filename: str) -> None:
    """
    Remove any blank lines from a file.

    Parameters
    ----------
    filename : str
        The file that will be 'cleaned.'
    """
    with open(filename, "r") as infile:
        all_lines = infile.readlines()

    with open(filename, "w") as outfile:
        outfile.writelines(line for line in all_lines if len(line) > 1)


def add(x: float, y: float) -> float:
    result = x + y
    return round(result, 2)


def convert_to_float(value: str) -> float:
    try:
        result = float(value)
    except ValueError:
        result = 0.00

    return result

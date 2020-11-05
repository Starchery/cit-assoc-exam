def clean_file(fname: str) -> None:
    """
    Remove any blank lines from a file.

    Parameters
    ----------
    fname : str
        The file that will be 'cleaned.'
    """
    with open(fname, "r") as infile:
        all_lines = infile.readlines()

    with open(fname, "w") as outfile:
        outfile.writelines(line for line in all_lines if len(line) > 1)


def add(x: float, y: float) -> float:
    result = x + y
    return round(result, 2)


def convert_to_float(value: str) -> float:
    if not value:  # if the string is empty
        return 0.00
    else:
        return float(value)

import csv

from typing import Dict, List
from . import utils

top_row = []


def read_csv(fname: str) -> Dict[str, List[float]]:
    result = {}
    with open(fname, "r") as csv_file:
        rows = csv.reader(csv_file)

        rows = filter(lambda row: row[0] != "Total", rows)  # skip the last row
        rows = map(lambda row: row[:-1], rows)  # skip the last column

        try:
            global top_row
            top_row = next(rows)  # skip the first row
        except StopIteration:
            pass

        for row in rows:
            category: str = row.pop(0)  # get and remove the first value
            result[category] = [utils.convert_to_float(value) for value in row]

    return result


def merge_csv(left, right) -> Dict[str, List[float]]:
    result = left.copy()
    for category, r_values in right.items():
        if category not in result:
            result[category] = r_values
        else:  # we have a common row that we need to merge
            # pair up corresponding values in left and right dicts
            pairs = zip(left[category], r_values)
            # add them to the left dict by adding up each pair of values
            result[category] = [utils.add(l, r) for (l, r) in pairs]
    return result


def write_csv(fname: str, sheet) -> None:
    with open(fname, "w") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(top_row)
        for category, values in sheet.items():
            values.insert(0, category)
            writer.writerow(values)

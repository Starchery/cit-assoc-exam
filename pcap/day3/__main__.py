from pcap.day3 import csv_parser, utils


def main():
    try:
        a_csv = csv_parser.read_csv("data/a.csv")
        b_csv = csv_parser.read_csv("data/b.csv")
    except FileNotFoundError as err:
        print(f"Bad filename: {err.filename}")
        return
    except OSError as err:
        print(f"Uhhhhhh {err}")
        return

    result_csv = csv_parser.merge_csv(a_csv, b_csv)
    csv_parser.write_csv("data/result2.csv", result_csv)

    try:
        utils.clean_file("data/result2.csv")
    except OSError as err:
        print(f"I found an error: {err}")


main()

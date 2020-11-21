from pcap.day03 import csv_parser, utils


def main():
    try:
        a_csv = csv_parser.read_csv("data/a.csv")
        b_csv = csv_parser.read_csv("data/b.csv")
    except FileNotFoundError as err:
        print(f"Bad filename: {err.filename}")
        return
    except utils.EmptyFile as err:
        print(err)
        return
    except OSError as err:
        print(f"Uhhhhhh {err}")
        return

    result_csv = csv_parser.merge_csv(a_csv, b_csv)

    try:
        csv_parser.write_csv("data/result3.csv", result_csv)
        utils.clean_file("data/result3.csv")
    except OSError as err:
        print(f"I found an error: {err}")


if __name__ == "__main__":
    main()

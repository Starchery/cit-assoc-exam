from pcap.day3 import csv_parser, utils


def main():
    a_csv = csv_parser.read_csv("data/a.csv")
    b_csv = csv_parser.read_csv("data/b.csv")

    result_csv = csv_parser.merge_csv(a_csv, b_csv)
    csv_parser.write_csv("data/result.csv", result_csv)

    utils.clean_file("data/result.csv")


main()

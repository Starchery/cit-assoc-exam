def uppercase(s: str) -> str:
    return s.upper()


def main():
    data = open("data/data.txt", "r")
    print(type(data))

    data = map(uppercase, data)
    print(type(data))


if __name__ == "__main__":
    main()

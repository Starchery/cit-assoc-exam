from time import time


def outer(arg):
    x = 1

    def inner():
        print(x + 1)

    inner()
    return inner


def timer(func):
    def wrapper(n: int):
        start = time()
        result = func(n)
        end = time()
        print(f"Took {end - start:.2f} seconds")
        return result

    return wrapper


# Higher order functions
# Treating functions like any other type of data

# Lambda functions


def mymap(func, lst):
    result = []
    for elem in lst:
        print(elem)
        new_elem = func(elem)
        result.append(new_elem)
    return result


def myfilter(predicate, lst):
    for elem in lst:
        if not predicate(elem):
            continue
        yield elem


def create_logger(program_name: str):
    def logger(message: str):
        print(f"[{program_name}] {message}")

    return logger


def main():
    pcaplogger = create_logger("pcap")
    citlogger = create_logger("cit")
    x = 3
    pcaplogger("Assigned x to 3")  # [pcap] Assigned x to 3
    x += 1
    citlogger("Assigned x+1 to x")  # [pcap] Assigned x+1 to x


if __name__ == "__main__":
    main()

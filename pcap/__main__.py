# Returns a list of numbers
# from 1 to n
# for some integer n
# numbers(10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from typing import Iterator, List


def numbers(n: int) -> List[int]:
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result


def number_generator(n: int) -> Iterator[int]:
    for num in range(1, n + 1):
        yield num


for num in number_generator(2 ** 98):
    print(f"I found {num}")

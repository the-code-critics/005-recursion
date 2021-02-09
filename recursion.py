"""
Some very simple examples of recursive functions to play with.
"""


def ones():
    print(1)
    ones()


def print_one(n):
    if n <= 0:
        return
    print(1)
    print_one(n - 1)


def list_of_ones(n):
    if n <= 0:
        return []
    return [1] + list_of_ones(n - 1)


def mk_list(item, n):
    if n <= 0:
        return []
    return [item] + mk_list(item, n - 1)


def numbers_up(start, n):
    if n <= 0:
        return []
    return [start] + numbers_up(start + 1, n - 1)


def numbers_down(start, n):
    if n <= 0:
        return []
    return numbers_down(start + 1, n - 1) + [start]


if __name__ == '__main__':
    import sys

    print('recursion limit', sys.getrecursionlimit())
    sys.setrecursionlimit(10)

    print(mk_list('a', 5))
    print(numbers_up(1, 5))
    print(numbers_down(1, 5))

    ones()

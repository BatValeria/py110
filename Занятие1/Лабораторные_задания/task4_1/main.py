from itertools import count


def task():
    counter = count(100, 10)

    for index in range(10):
        4print(next(counter))# TODO распечатать с столбик первые 10 чисел бесконечного итератора


if __name__ == "__main__":
    task()

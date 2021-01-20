import sys
import time

from tests import hello


def add(x, y):
    time.sleep(1)
    return x + y


def add_array(array):
    if len(array) > 1:
        result = add(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = add(result, int(array[i]))
        return result
    return None


def subtract(x, y):
    time.sleep(1)
    return x - y


def subtract_array(array):
    if len(array) > 1:
        result = subtract(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = subtract(result, int(array[i]))
        return result
    return None


def multiply(x, y):
    time.sleep(1)
    return x * y


def multiply_array(array):
    if len(array) > 1:
        result = multiply(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = multiply(result, int(array[i]))
        return result
    return None


def divide(x, y):
    time.sleep(1)
    return x / y


def divide_array(array):
    if len(array) > 1:
        result = divide(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = divide(result, int(array[i]))
        return result
    return None


def main(args):
    add_array(args)
    subtract_array(args)
    multiply_array(args)
    divide_array(args)
    hello.new_func()


if __name__ == "__main__":
    main(sys.argv[1:])

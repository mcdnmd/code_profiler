import sys
import time


def add(x, y):
    return x + y


def add_array(array):
    time.sleep(1)
    if len(array) > 1:
        result = add(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = add(result, int(array[i]))
        return result
    return None


def subtract(x, y):
    return x - y


def subtract_array(array):
    time.sleep(1)
    if len(array) > 1:
        result = subtract(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = subtract(result, int(array[i]))
        return result
    return None


def multiply(x, y):
    return x * y


def multiply_array(array):
    time.sleep(1)
    if len(array) > 1:
        result = multiply(int(array[0]), int(array[1]))
        for i in range(2, len(array)):
            result = multiply(result, int(array[i]))
        return result
    return None


def divide(x, y):
    return x / y


def divide_array(array):
    time.sleep(1)
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


if __name__ == "__main__":
    main(sys.argv[1:])

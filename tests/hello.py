import time


def sleep_for_4_sec():
    time.sleep(4)


def sleep_for_2_sec():
    time.sleep(2)


def main():
    sleep_for_4_sec()
    sleep_for_2_sec()


def new_func():
    sleep_for_2_sec()
    sleep_for_2_sec()
    time.sleep(2)


if __name__ == '__main__':
    main()
    new_func()

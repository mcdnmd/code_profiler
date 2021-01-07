import time


def sleep_for_5_sec():
    time.sleep(5)


def sleep_for_10_sec():
    time.sleep(10)


def sleep_for_2_sec():
    time.sleep(2)


def main():
    sleep_for_5_sec()
    sleep_for_2_sec()
    sleep_for_10_sec()


if __name__ == '__main__':
    main()

import argparse


def parse_terminal_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'program_path',
        action='store',
        help='path to profiling file')
    parser.add_argument(
        'program_args',
        nargs='+',
        type=int)

    return parser.parse_args()
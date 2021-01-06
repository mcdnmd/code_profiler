import os
import sys
import time
import traceback
import threading
import argparse
from modules.Profiler import Profiler


PATH = os.path.dirname(__file__)


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'program_path',
        action='store',
        type=str,
        help='file/script path')
    parser.add_argument(
        '-a',
        action='store',
        dest='program_args',
        nargs='+',
        default=None,
        type=int,
        help='file`s/script`s arguments')

    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    if len(args.__dict__) > 0:
        name = args.program_path
        arguments = args.program_args
        globs = {
            '__file__': os.path.join(PATH, name),
            '__name__': '__main__',
            '__package__': None,
            '__cached__': None,
        }
        p = Profiler(globs, arguments)
        p.start()
    else:
        parser.print_usage()
        sys.exit(2)


if __name__ == '__main__':
    main()

import os
import sys
import time
import traceback
import threading
import argparse
from modules.Profiler import Profiler

PATH = os.path.dirname(__file__)


def program_path(input_data):
    if input_data.startswith('.'):
        path = PATH + os.path.dirname(input_data[1:])
        return os.path.join(path, os.path.basename(input_data))
    elif input_data.startswith('/'):
        if os.path.isfile(input_data):
            return input_data
        else:
            raise Exception("File not exists")
    return os.path.join(PATH, input_data)


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('program_path', action='store', type=program_path,
                        help='file/script path')
    parser.add_argument('-a', action='store', dest='program_args', nargs='+',
                        default=None, type=int,
                        help='file`s/script`s arguments')

    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    if len(args.__dict__) > 0:
        name = args.program_path
        arguments = args.program_args
        globs = {'__file__': args.program_path, '__name__': '__main__',
                 '__package__': None, '__cached__': None, }
        p = Profiler(globs, arguments)
        p.start()
    else:
        parser.print_usage()
        sys.exit(2)


if __name__ == '__main__':
    main()

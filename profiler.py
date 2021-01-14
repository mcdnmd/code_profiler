import os
import sys
import time
import traceback
import threading
import argparse
from modules.Core import ProfilerCore

PATH = os.path.dirname(os.path.abspath(__file__))


def workdir_path(input_data):
    print(PATH, input_data)
    if input_data.startswith('.'):
        return PATH + input_data[1:]
    elif input_data.startswith('/'):
        if os.path.isdir(input_data):
            return input_data
        else:
            os.makedirs(input_data, exist_ok=True)
    return input_data


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w',
                        dest='workdir',
                        action='store',
                        type=workdir_path,
                        help='work directory path')
    parser.add_argument('-s',
                        dest='sortby',
                        action='store',
                        default=None,
                        type=str,
                        help='chose sort by parameter (default: time)')
    parser.add_argument('-o',
                        dest='output',
                        action='store',
                        default=None,
                        type=str,
                        help='chose file for output (default: ...)')
    parser.add_argument('-i',
                        dest='interval',
                        action='store',
                        default=10,
                        type=int,
                        help='chose interval in ms (default: 10ms)')
    parser.add_argument('program',
                        action='store',
                        type=str,
                        help='name for program e.g. hello.py')
    parser.add_argument('-a',
                        dest='argv',
                        action='store',
                        nargs='+',
                        default=None,
                        help='program arguments')
    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    if len(args.__dict__) > 0:
        progname = args.program
        arguments = args.argv
        workdir = args.workdir
        sortby = args.sortby
        output = args.output
        interval = args.interval
        globs = {'__file__': progname,
                 '__name__': '__main__',
                 '__package__': None,
                 '__cached__': None, }
        p = ProfilerCore(globs, arguments, workdir, sortby, output, interval)
        p.start()
    else:
        parser.print_usage()
        sys.exit(2)


if __name__ == '__main__':
    main()

import os
import csv
import argparse

from modules.OutputFormatter import OutputFormatter
from modules.StatisticCalculator import StatisticCalculater


def file_name(name):
    if os.path.exists(name):
        return name
    else:
        raise FileNotFoundError


def get_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file',
        action='store',
        type=file_name,
        metavar='.csv',
        help='name of `raw` profiling statistics')
    parser.add_argument(
        '-s',
        dest='sortby',
        action='store',
        default='time',
        type=str,
        help='chose sort by parameter (default: time)'
    )
    return parser


def parse_str_to_array(string):
    result = []
    tuples = []

    start = 0
    stop = 0

    for i in range(len(string)):
        if string[i] == '(':
            start = i + 1
        elif string[i] == ')':
            stop = i
            tuples.append(string[start:stop])

    for tup in tuples:
        tup = tup.replace('\'', '')
        tup = tup.replace(' ', '')
        tup = tup.split(',')
        func_name = tup[0]
        lineno = int(tup[1])
        result.append((func_name, lineno))

    return result


def parse_str_to_dict(string):
    result = {}
    string = string[1:-1]
    string = string.replace(' ', '')
    string = string.replace('\'', '')
    string = string.split(',')
    for pair in string:
        pair = pair.split(':')
        for i in range(len(pair)-1):
            result[pair[i]] = pair[i+1]

    return result



def get_correct_type_raw_data(file_name):
    result = []
    with open(file_name) as csv_file:
        title_flag = True
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if not title_flag:
                frame_num = int(line[0])
                lineno = int(line[2])
                called_from = []
                tmp_called_from = line[4]
                array = parse_str_to_array(tmp_called_from)
                for func, lineno in array:
                    called_from.append((func, int(lineno)))
                time_step = float(line[5])
                args = parse_str_to_dict(line[6])
                result.append((frame_num, line[1], lineno, line[3], called_from,
                               time_step, args))
            else:
                title_flag = False
    return result


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    stat_calculator = StatisticCalculater()

    raw_data = get_correct_type_raw_data(args.file)

    stat_calculator.update_raw_data(raw_data)
    calculated_stat = stat_calculator.calc_statistics()

    o = OutputFormatter(stat_calculator.prog_name, args.sortby)
    o.intro()
    o.create_output(calculated_stat)



if __name__ == '__main__':
    main()
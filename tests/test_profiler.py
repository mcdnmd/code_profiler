import os
import unittest

from modules import Profiler

PATH = os.path.dirname(__file__)
RESULT_1 = {'sleep_for_2_sec': 12, 'sleep_for_5_sec': 29,
            'sleep_for_10_sec': 59}

RESULT_2 = {'add_array': 25, 'subtract_array': 25, 'multiply_array': 25,
            'divide_array': 25}


class ProfilerTestLogic(unittest.TestCase):
    def test_simple_program(self):
        name = 'hello.py'
        globs = {'__file__': os.path.join(PATH, name), '__name__': '__main__',
                 '__package__': None, '__cached__': None, }

        p = Profiler.Profiler(globs)
        p.start()

        while Profiler.FLAG:
            continue

        for key in p.stat.keys():
            p.stat[key] = round(p.stat[key])

        for key in p.stat.keys():
            self.assertTrue(abs(p.stat[key] - RESULT_1[key]) <= 2)

    def test_program_with_args(self):
        name = 'calculater.py'
        args = [36, 23, 571, 74654]
        globs = {'__file__': os.path.join(PATH, name), '__name__': '__main__',
                 '__package__': None, '__cached__': None}
        p = Profiler.Profiler(globs, args, 1 / 1000)
        p.start()

        while Profiler.FLAG:
            continue

        for key in p.stat.keys():
            p.stat[key] = round(p.stat[key])

        for key in p.stat.keys():
            self.assertTrue(abs(p.stat[key] - RESULT_2[key]) <= 2)

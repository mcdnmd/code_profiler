import os
import unittest

from modules.Core import ProfilerCore

PATH = os.path.dirname(__file__)
RESULT_1 = {'sleep_for_2_sec': 3, 'sleep_for_4_sec': 2, 'main': 1,
            'new_func': 1, '<module>': 1}


class ProfilerTestLogic(unittest.TestCase):
    def test_simple_program(self):
        globs = {'__file__': 'hello.py', '__name__': '__main__',
                 '__package__': None, '__cached__': None, }

        core = ProfilerCore(globs, [], PATH, None, None, 10)
        core.start()

        statistics = core.prog_statistics.funcs
        for func in statistics.keys():
            self.assertEqual(RESULT_1[func],
                             len(statistics[func].worked_time_steps))

    def test_program_with_args(self):
        args = [36, 23, 571, 74654]
        globs = {'__file__': 'calculater.py', '__name__': '__main__',
                 '__package__': None, '__cached__': None}
        core = ProfilerCore(globs, args, PATH, None, None, 1)
        core.start()

        statistics = core.prog_statistics.funcs
        self.assertEqual(10, len(statistics))

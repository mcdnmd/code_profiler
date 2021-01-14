import csv
import os

from modules.Profiler import Profiler
from modules.Statistics import ProgStatistics


class ProfilerCore:
    def __init__(self, globs, argv, workdir, sortby, output, interval):
        self.globs = globs
        self.argv = argv
        self.workdir = workdir
        self.sortby = sortby
        self.output = output
        self.interval = interval
        self.prog_name = globs['__file__']
        self.prog_statistics = ProgStatistics(self.prog_name)

        self.globs['__file__'] = os.path.join(self.workdir, self.prog_name)

    def start(self):
        self.Profiler = Profiler(self.globs, self.argv, self.interval)
        self.Profiler.start()
        self.calculate_statistics()
        if self.output is not None:
            self.create_an_output()

    def calculate_statistics(self):
        counter = 0
        time_per_screen = self.Profiler.worked_time / len(
            self.Profiler.stack_screens)
        for stack in self.Profiler.stack_screens:
            called_from = 'func'
            for frame in stack:
                filename = os.path.basename(frame[0])
                if filename == self.prog_name:
                    line_number = frame[1]
                    func_name = frame[2]
                    self.prog_statistics.update_statistics(func_name,
                                                           time_per_screen,
                                                           counter,
                                                           called_from)
                    called_from = func_name
            counter += 1

        for func, statistics in self.prog_statistics.funcs.items():
            statistics.worked_time_steps.append(statistics.step_worked_time)
            statistics.calc_sub_metrics()

    def create_an_output(self):
        filename = os.path.join(self.workdir, f'{self.output}.csv')
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['func', 'amount_time', 'max', 'min', 'median'])
            for func, statistics in self.prog_statistics.funcs.items():
                writer.writerow([func, statistics.amount_worked_time,
                                 statistics.worked_time_max,
                                 statistics.worked_time_min,
                                 statistics.worked_time_median])

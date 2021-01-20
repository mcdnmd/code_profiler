import csv
import os

from modules.OutputFormatter import OutputFormatter
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

        if self.output is not None:
            self.save_raw_data(self.Profiler.raw_data)
            filename = os.path.join(self.workdir, f'{self.output}.csv')
            print(f'Raw data was saved in {filename}')
            return

        self.calc_statistics()
        o = OutputFormatter(self.prog_name, self.sortby)
        o.intro()
        o.create_output(self.prog_statistics.funcs)

    def calc_statistics(self):
        for raw_line in self.Profiler.raw_data:
            self.prog_statistics.update_statistics(raw_line)
        self.prog_statistics.final_calc()

    def save_raw_data(self, data):
        filename = os.path.join(self.workdir, f'{self.output}.csv')
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['time_step', 'filename', 'lineno', 'function', 'called_order',
                 'time_per_step', 'args'])
            for func in data:
                writer.writerow(func)

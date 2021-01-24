from modules.Statistics import ProgStatistics


class StatisticCalculater:
    def __init__(self):
        self.prog_statistics = ProgStatistics()
        self.raw_data = None
        self.prog_name = None

    def update_raw_data(self,  raw_data):
        self.raw_data = raw_data

    def calc_statistics(self):
        for raw_line in self.raw_data:
            if self.prog_name is None:
                self.extract_prog_name(raw_line)
            self.prog_statistics.update_statistics(raw_line)
        self.prog_statistics.final_calc()
        return self.prog_statistics.funcs

    def extract_prog_name(self, line):
        if len(line[1]) > 0:
            self.prog_name = line[1]
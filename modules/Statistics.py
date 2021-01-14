import sys


class ProgStatistics:
    def __init__(self, filename):
        self.filename = filename
        self.funcs = {}

    def update_statistics(self, func_name, time, screen_number, called_from):
        try:
            self.funcs[func_name].update_statistics(time, screen_number,
                                                    called_from)
        except KeyError:
            self.funcs[func_name] = FuncStatistics(func_name, screen_number,
                                                   called_from)
            self.funcs[func_name].update_statistics(time, screen_number,
                                                    called_from)


class FuncStatistics:
    def __init__(self, func_name, screen_number, called_from):
        self.func_name = func_name
        self.calls = 0
        self.worked_time_min = 10 ** 9
        self.worked_time_max = 0
        self.worked_time_median = 0
        self.amount_worked_time = 0
        self.step_worked_time = 0
        self.worked_time_steps = []
        self.last_screen = screen_number
        self.called_from = called_from

    def update_statistics(self, time, screen_number, called_from):

        if screen_number - self.last_screen < 2 and self.called_from == \
                called_from:
            self.step_worked_time += time
            self.last_screen = screen_number
        else:
            self.worked_time_steps.append(self.step_worked_time)
            self.step_worked_time = time
            if called_from != self.called_from:
                self.called_from = called_from
            self.last_screen = screen_number

    def calc_sub_metrics(self):
        if len(self.worked_time_steps) != 0:
            for time in self.worked_time_steps:
                self.amount_worked_time += time

                if time > self.worked_time_max:
                    self.worked_time_max = time
                if time < self.worked_time_min:
                    self.worked_time_min = time
            self.worked_time_median = self.amount_worked_time / len(
                self.worked_time_steps)

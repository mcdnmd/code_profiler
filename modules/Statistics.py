import statistics

class ProgStatistics:
    def __init__(self):
        self.funcs = {}

    def update_statistics(self, func):
        step_number = func[0]
        f_lineno = func[2]
        f_name = func[3]
        f_called_order = func[4]
        f_time_step = func[5]
        f_args = func[6]
        self._update(f_name, step_number, f_called_order, f_time_step, f_args)
        self.cum_update(step_number, f_called_order, f_time_step)

    def cum_update(self, step_number, called_order, time_step):
        for i in range(len(called_order) - 1, -1, -1):
            call = called_order[i]
            f_name, f_lineno = call[0], call[1]
            try:
                self.funcs[f_name].cumtime += time_step
            except KeyError:
                self.funcs[f_name] = FuncStatistics(step_number, [], [])
                self.funcs[f_name].cumtime += time_step

    def final_calc(self):
        for value in self.funcs.values():
            value.sub_calc()
            for f_name in value.was_called_from:
                self.funcs[f_name].tottime -= value.cumtime
        for value in self.funcs.values():
            value.final_calc()

    def _update(self, name, step_number, called_order, time_step, args):
        try:
            self.funcs[name].update_statistics(step_number, called_order,
                                               time_step, args)
        except KeyError:
            self.funcs[name] = FuncStatistics(step_number, called_order, args)
            self.funcs[name].update_statistics(step_number, called_order,
                                               time_step, args)


class FuncStatistics:
    def __init__(self, step_number, called_order, args):
        self.last_step = step_number
        self.ncalls = 1
        self.tottime = 0
        self.percall1 = 0
        self.percall2 = 0
        self.cumtime = 0
        self.maxtime = 0
        self.mintime = 0
        self.medtime = 0
        self.called_order = called_order
        self.was_called_from = set()
        self.current_period = 0
        self.args = args
        self.worked_times = []

    def update_statistics(self, step_number, called_order, time_step, args):

        SAME_CALL = self.check_same_conditions(step_number, called_order, args)

        if SAME_CALL:
            self.current_period += time_step
            self.last_step = step_number

        else:
            self.ncalls += 1
            if self.current_period > 0:
                self.worked_times.append(self.current_period)

            for func in self.called_order:
                self.was_called_from.add(func[0])
            self.called_order = called_order
            self.args = args
            self.current_period = 0
            self.last_step = step_number

    def check_same_conditions(self, step_number, called_order, args):
        if step_number - self.last_step > 1:
            return False
        if len(self.called_order) != len(called_order):
            return False
        for i in range(len(called_order)):
            for j in range(2):
                if self.called_order[i][j] != called_order[i][j]:
                    return False

        if len(self.args) != len(args):
            return False
        for key, value in args.items():
            try:
                result = self.args[key]
            except KeyError:
                return False
            if result != value:
                return False
        return True

    def sub_calc(self):
        if self.current_period > 0:
            self.worked_times.append(self.current_period)
            for func in self.called_order:
                self.was_called_from.add(func[0])
        self.cumtime = round(self.cumtime + sum(self.worked_times), 2)

    def final_calc(self):
        self.tottime = round(self.tottime + self.cumtime, 2)
        if self.tottime < 0:
            self.tottime = 0
        else:
            self.tottime = round(self.tottime, 2)
        self.percall1 = round(self.cumtime / self.ncalls, 2)
        self.percall2 = round(self.tottime / self.ncalls, 2)
        if len(self.worked_times) > 0:
            self.maxtime = round(max(self.worked_times), 3)
            self.mintime = round(min(self.worked_times), 3)
            self.medtime = round(statistics.median(self.worked_times), 3)

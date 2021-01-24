class OutputFormatter:
    def __init__(self, filename, sortby):
        self.filename = filename
        self.sortby = sortby

    def intro(self):
        print(f'  Ordered by: {self.sortby}')
        header = ['ncalls', 'tottime', 'percall', 'cumtime', 'percall',
                  'maxtime', 'mintime', 'medtime', 'filename:(function)']

        for column in header:
            print(f"{column: >8}", end=" ")
        print()

    def create_output(self, stats):
        sorted_output = self.sort_output(stats)
        for key, value in sorted_output.items():
            ncalls = value.ncalls
            tottime = value.tottime
            percall1 = value.percall1
            percall2 = value.percall2
            cumtime = value.cumtime
            maxtime = value.maxtime
            mintime = value.mintime
            medtime = value.medtime
            print(f"{ncalls: >8}"
                  f" {tottime: >8}"
                  f" {percall2: >8}"
                  f" {cumtime: >8}"
                  f" {percall1: >8}"
                  f" {maxtime: >8}"
                  f" {mintime: >8}"
                  f" {medtime: >8}"
                  f" {self.filename}:({key})", end="\n")

    def sort_output(self, stats):
        if self.sortby == 'time':
            return dict(sorted(stats.items(), key=lambda item: item[1].cumtime,
                               reverse=True))
        elif self.sortby == 'calls':
            return dict(sorted(stats.items(), key=lambda item: item[1].ncalls,
                               reverse=True))
        elif self.sortby == 'percall':
            return dict(sorted(stats.items(), key=lambda item: item[1].percall,
                               reverse=True))
        else:
            return stats

import sys
import threading
import time
import traceback

FLAG = True


def run(code, globs):
    global FLAG
    try:
        exec(code, globs)
    except Exception as e:
        print(e)
        raise
    FLAG = False


def calculate_time(work_time, stat):
    calls = 0
    for value in stat.values():
        calls += value

    time_per_call = work_time / calls

    for key in stat.keys():
        stat[key] *= time_per_call / work_time * 100

    for key, value in stat.items():
        print(f'func {key} worked {round(value, 2)}% of time')


class Profiler:
    def __init__(self, globs, args=None):
        self.globs = globs

        with open(globs['__file__'], 'rb') as fp:
            self.code = compile(fp.read(), 'executed_file', 'exec')

        self.args = args
        self.profile_object = threading.Thread(target=run,
                                               args=[self.code, self.globs],
                                               daemon=True)

    def start(self):
        start_time = time.time()
        self.profile_object.start()
        threadId = self.profile_object.ident

        stat = {}

        while FLAG:
            time.sleep(1/20)
            for id, stack in sys._current_frames().items():
                if id == threadId:
                    call_stack = []
                    for frame in traceback.extract_stack(stack):
                        filename = frame[0]
                        line = frame[3]
                        lineno = frame[1]
                        name = frame[2]
                        if filename == 'executed_file':
                            call_stack.append(name)

                    if call_stack:
                        last_call = call_stack.pop(len(call_stack) - 1)
                        try:
                            stat[last_call] += 1
                        except KeyError:
                            stat[last_call] = 0
        work_time = time.time() - start_time
        calculate_time(work_time, stat)

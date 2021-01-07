import sys
import threading
import time
import traceback

FLAG = True


def run(code, globs, args):
    global FLAG
    try:
        sys.argv = args
        exec(code, globs)
    except Exception as e:
        print(e)
        FLAG = False
        raise

    FLAG = False


def calculate_time(work_time, stat):
    calls = 0
    for value in stat.values():
        calls += value
    if calls == 0:
        return
    time_per_call = work_time / calls

    for key in stat.keys():
        stat[key] *= time_per_call / work_time * 100

    for key, value in stat.items():
        print(f'func {key} worked {round(value, 2)}% of time')


class Profiler:
    def __init__(self, globs, args=None, interval=1/60,):
        self.globs = globs
        self.interval = interval

        with open(globs['__file__'], 'rb') as fp:
            self.code = compile(fp.read(), 'executed_file', 'exec')

        self.args = [globs['__file__']]
        if args is not None:
            for a in args:
                self.args.append(a)

        self.profile_object = threading.Thread(target=run,
                                               args=[self.code,
                                                     self.globs,
                                                     self.args],
                                               daemon=True)
        self.stat = {}

    def start(self):
        start_time = time.time()
        self.profile_object.start()
        profiling_thread_id = self.profile_object.ident

        while FLAG:
            time.sleep(self.interval)
            for thread_id, stack in sys._current_frames().items():
                if thread_id == profiling_thread_id:
                    call_stack = []
                    for frame in traceback.extract_stack(stack):
                        filename = frame[0]
                        name = frame[2]
                        if filename == 'executed_file':
                            call_stack.append(name)

                    if call_stack:
                        last_call = call_stack.pop(len(call_stack) - 1)
                        try:
                            self.stat[last_call] += 1
                        except KeyError:
                            self.stat[last_call] = 0

        work_time = time.time() - start_time
        calculate_time(work_time, self.stat)

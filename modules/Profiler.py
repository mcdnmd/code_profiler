import os
import sys
import threading
import time
import traceback

FILENAME = os.path.abspath(__file__)
FLAG = True


def worker(code, globs, args):
    global FLAG
    try:
        sys.argv = args
        exec(code, globs)
    except Exception as e:
        print(e)
        FLAG = False
        raise
    FLAG = False


class Profiler:
    def __init__(self, globs, args, interval):
        self.globs = globs
        self.interval = 1 / 1000 * interval

        with open(globs['__file__'], 'rb') as fp:
            self.code = compile(fp.read(), globs['__file__'], 'exec')

        self.args = [globs['__file__']]
        if args is not None:
            for a in args:
                self.args.append(a)

        self.profile_object = threading.Thread(target=worker,
                                               args=[self.code, self.globs,
                                                     self.args], daemon=True)
        self.stack_screens = []
        self.worked_time = 0

    def start(self):
        self.worked_time = time.time()
        self.profile_object.start()
        profiling_thread_id = self.profile_object.ident

        try:
            self.main_loop(profiling_thread_id)
        except KeyboardInterrupt:
            self.worked_time = time.time() - self.worked_time
            return
        self.worked_time = time.time() - self.worked_time

    def main_loop(self, profiling_thread_id):
        stack_search_time = 0
        while FLAG:
            if self.interval - stack_search_time > 0:
                time.sleep(self.interval - stack_search_time)

            time_start = time.time()

            for thread_id, stack in sys._current_frames().items():
                if thread_id == profiling_thread_id:
                    call_stack = []
                    see_stack = False
                    for frame in traceback.extract_stack(stack):
                        filename = frame[0]
                        if filename == FILENAME:
                            see_stack = True
                            continue
                        if see_stack:
                            call_stack.append(frame)

                    if call_stack:
                        self.stack_screens.append(call_stack)

            stack_search_time = time.time() - time_start

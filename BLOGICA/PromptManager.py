from threading import Thread, enumerate, Event
from queue import Queue, Empty
import time

from inputimeout import inputimeout, TimeoutOccurred
from pynput.keyboard import Key, Controller


SENTINEL = None


class PromptManager(Thread):

    def __init__(self, timeout):
        super().__init__()
        self.timeout = timeout
        self._in_queue = Queue()
        self._out_queue = Queue()
        self.prompter = Thread(target=self._prompter, daemon=True)
        self._prompter_exit = Event()

    def run(self):
        """Run worker-thread. Start prompt-thread, fetch passed
        input from in_queue and forward it to `._poll()` in MainThread.
        If timeout occurs before user-input, enqueue SENTINEL to
        unblock `.get()` in `._poll()`.
        """
        self.prompter.start()
        try:
            txt = self._in_queue.get(timeout=self.timeout)
        except Empty:
            self._out_queue.put(SENTINEL)
            # without usage of _prompter_exit() and Enter, the
            # prompt-thread would stay alive until the whole program ends
            keyboard = Controller()
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            self._prompter_exit.wait()
        else:
            self._out_queue.put(txt)

    def start(self):
        """Start manager-thread."""
        super().start()
        return self._poll()

    def _prompter(self):
        """Prompting target function for execution in prompter-thread."""
        try:
            self._in_queue.put(inputimeout(f"[{time.ctime()}] >$ ", timeout=5))
            self._prompter_exit.set()
        except TimeoutOccurred:
            print('timeout')
            self._prompter_exit.set()

    def _poll(self):
        """Get forwarded inputs from the manager-thread executing `run()`
        and process them in the parent-thread.
        """
        msg =  self._out_queue.get()
        self.join()
        return msg
import os
import signal


def suspend_thread(tid: int) -> None:
    os.kill(tid, signal.SIGSTOP)


def resume_thread(tid: int) -> None:
    os.kill(tid, signal.SIGCONT)

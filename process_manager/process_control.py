import os
import signal


def create_process(command: list, priority: int = 0) -> int:
    print(command)
    pid = os.fork()
    if pid == 0:
        os.nice(priority)
        os.execvp(command[0], command)
    return pid


def kill_process_tree(pid: int) -> None:
    try:
        os.kill(pid, signal.SIGTERM)
        _, _ = os.waitpid(pid, 0)
    except OSError:
        pass

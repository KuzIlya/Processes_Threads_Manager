import os
import pwd
from typing import Any


def get_process_info(pid: int) -> dict[str, Any] | None:
    try:

        with open(f"/proc/{pid}/status") as f:
            lines = f.readlines()

        info = {
            line.split(":")[0]: line.split(":")[1].strip()
            for line in lines
            if ':' in line
        }

        mem = info.get("VmRSS", "0 kB")
        threads = info.get("Threads", "0")
        uid = info.get("Uid", "0").split()[0]
        user = pwd.getpwuid(int(uid)).pw_name

        with open(f"/proc/{pid}/maps") as f:
            modules = set(line.split()[-1] for line in f if '/' in line)

        return {
            "memory": mem,
            "threads": threads,
            "user": user,
            "modules": list(modules)
        }

    except FileNotFoundError:
        return None


def get_priority(pid: int) -> int:
    return os.getpriority(os.PRIO_PROCESS, pid)


def set_priority(pid: int, priority: int) -> None:
    os.setpriority(os.PRIO_PROCESS, pid, priority)

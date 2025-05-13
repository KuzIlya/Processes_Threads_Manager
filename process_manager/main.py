import argparse

from .process_control import create_process, kill_process_tree
from .process_tree import display_process_tree
from .process_info import get_process_info, set_priority, get_priority
from .thread_control import suspend_thread, resume_thread


parser = argparse.ArgumentParser(description="POSIX Process Manager")

subparsers = parser.add_subparsers(dest="command")

sp_create = subparsers.add_parser("create")
sp_create.add_argument("command", nargs='+')
sp_create.add_argument("--priority", type=int, default=0)

sp_kill = subparsers.add_parser("kill")
sp_kill.add_argument("pid", type=int)

sp_info = subparsers.add_parser("info")
sp_info.add_argument("pid", type=int)

sp_tree = subparsers.add_parser("tree")

sp_suspend = subparsers.add_parser("suspend")
sp_suspend.add_argument("tid", type=int)

sp_resume = subparsers.add_parser("resume")
sp_resume.add_argument("tid", type=int)

sp_priority = subparsers.add_parser("priority")
sp_priority.add_argument("pid", type=int)
sp_priority.add_argument("--set", type=int)


if __name__ == '__main__':

    args = parser.parse_args()

    match args.command:
        case "create":
            pid = create_process(args.command, args.priority)
            print(f"Created process with PID: {pid}")
        case "kill":
            kill_process_tree(args.pid)
            print(f"Killed process tree starting from PID: {args.pid}")
        case "info":
            info = get_process_info(args.pid)
            if info:
                print(f"Process Info [PID {args.pid}]:")
                for k, v in info.items():
                    print(f"  {k}: {v}")
            else:
                print("Process not found.")
        case "tree":
            display_process_tree()
        case "suspend":
            suspend_thread(args.tid)
            print(f"Suspended thread with TID: {args.tid}")
        case "resume":
            resume_thread(args.tid)
            print(f"Resumed thread with TID: {args.tid}")
        case "priority":
            if args.set is not None:
                set_priority(args.pid, args.set)
                print(f"Set priority of PID {args.pid} to {args.set}")
            else:
                prio = get_priority(args.pid)
                print(f"Priority of PID {args.pid}: {prio}")
        case _:
            parser.print_help()


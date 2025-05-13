import subprocess


def display_process_tree() -> None:
    result = subprocess.run(
        ['ps', '-eo', 'pid,ppid,comm'],
        capture_output=True,
        text=True,
    )
    lines = result.stdout.strip().split('\n')[1:]
    processes = [line.split(maxsplit=2) for line in lines]

    tree = {}
    for pid, ppid, name in processes:
        tree.setdefault(ppid, []).append((pid, name))

    def print_tree(pid: int, prefix: str = '') -> None:
        children = tree.get(pid, [])
        for child_pid, name in children:
            print(f"{prefix}- {name} (PID: {child_pid})")
            print_tree(child_pid, prefix + "  ")

    print_tree('1')

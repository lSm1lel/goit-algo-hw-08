"""Послідовний запуск прикладів усіх трьох завдань."""

from task_1 import main as run_task_1
from task_2 import main as run_task_2
from task_3 import main as run_task_3


def main():
    run_task_1()
    print()
    run_task_2()
    print()
    run_task_3()


if __name__ == "__main__":
    main()

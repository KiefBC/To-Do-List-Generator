from datetime import datetime, timedelta

import database
import instruction

TASK_MENU = """1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add a task\n0) Exit"""


def main():
    while True:
        try:
            ask_task = input(f"{TASK_MENU}\n")
            match ask_task:
                case "1":  # Today's tasks
                    instruction.daily_tasks()
                case "2":  # Week's tasks
                    instruction.weekly_tasks()
                case "3":  # All tasks
                    instruction.all_tasks()
                case "4":  # Add a task
                    instruction.add_task()
                case "0":
                    print("Bye!")
                    break
        except AttributeError:
            print("Invalid input!")
            continue


if __name__ == '__main__':
    db = database.ToDo()
    database.main()
    main()

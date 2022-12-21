import database
import instruction

TASK_MENU = """1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add a task\n6) Delete a task\n0) Exit """


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
                case "4":  # Missed tasks
                    instruction.missed_tasks()
                case "5":  # Add a task
                    instruction.add_task()
                case "6":  # Delete a task
                    instruction.delete_task()
                case "0":
                    print("\nBye!")
                    break
        except AttributeError:
            print("Invalid input!")
            continue


if __name__ == '__main__':
    db = database.ToDo()
    database.main()
    main()

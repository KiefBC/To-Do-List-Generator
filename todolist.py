from datetime import datetime, timedelta

import database

TASK_MENU = """1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add a task\n0) Exit"""


def main():
    while True:
        try:
            ask_task = input(f"{TASK_MENU}\n")
            match ask_task:
                case "1":  # Today's tasks
                    todays_tasks = database.session.query(database.ToDo).filter(database.ToDo.deadline == datetime.today().date()).all()
                    if len(todays_tasks) == 0:
                        print(datetime.today().strftime("\nToday %d %b:\nNothing to do!"))
                    for i, row in enumerate(todays_tasks):
                        print(f'{i + 1}. {row.task}')
                    print()
                case "2":  # Week's tasks
                    week_tasks = database.session.query(database.ToDo).filter(database.ToDo.deadline <= datetime.today().date() + timedelta(days=7)).all()
                    for i in range(7):
                        # Get the tasks for that day
                        day_tasks = [task for task in week_tasks if task.deadline == datetime.today().date() + timedelta(days=i)]
                        # Print the day and the tasks
                        print(f"\n{datetime.today().date() + timedelta(days=i):%A} {datetime.today().date() + timedelta(days=i):%d} {datetime.today().date() + timedelta(days=i):%b}:")
                        if len(day_tasks) == 0:
                            print("Nothing to do!")
                        for j, row in enumerate(day_tasks):
                            print(f'{j + 1}. {row.task}')
                    print()
                case "3":  # All tasks
                    all_tasks = database.session.query(database.ToDo).order_by(database.ToDo.deadline).all()
                    print()
                    if len(all_tasks) == 0:
                        print("\nNothing to do!")
                    for i, row in enumerate(all_tasks):
                        print(f'{i + 1}. {row.task}. {row.deadline:%d} {row.deadline:%b}')
                    print()
                case "4":  # Add a task
                    new_task = input("Enter task\n")
                    while True:  # Validate the date
                        try:
                            # We only accept dates in the format YYYY-MM-DD
                            new_deadline = datetime.strptime(input("Enter deadline\n"), "%Y-%m-%d")
                        except ValueError:
                            print("Invalid date format!")
                        else:
                            new_row = database.ToDo(task=new_task, deadline=new_deadline)
                            database.session.add(new_row)
                            database.session.commit()
                            print("The task has been added!\n")
                            break
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

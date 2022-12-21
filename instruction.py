import database
from datetime import datetime, timedelta

NEW_LINE = "\r"


def daily_tasks():
    tasks = database.session.query(database.ToDo).filter(database.ToDo.deadline == datetime.today().date()).all()
    if len(tasks) == 0:
        print(datetime.today().strftime("\nToday %d %b:\nNothing to do!"))
    for i, row in enumerate(tasks):
        print(f'{i + 1}. {row.task}')
    print(NEW_LINE)


def weekly_tasks():
    tasks = database.session.query(database.ToDo).filter(
        database.ToDo.deadline <= datetime.today().date() + timedelta(days=7)).all()
    for i in range(7):
        # Get the tasks for that day
        day_tasks = [task for task in tasks if task.deadline == datetime.today().date() + timedelta(days=i)]
        # Print the day and the tasks
        print(
            f"\n{datetime.today().date() + timedelta(days=i):%A} {datetime.today().date() + timedelta(days=i):%d} {datetime.today().date() + timedelta(days=i):%b}:")
        if len(day_tasks) == 0:
            print("Nothing to do!")
        for j, row in enumerate(day_tasks):
            print(f'{j + 1}. {row.task}')
    print(NEW_LINE)


def all_tasks():
    tasks = database.session.query(database.ToDo).order_by(database.ToDo.deadline).all()
    print(NEW_LINE)
    if len(tasks) == 0:
        print("\nNothing to do!")
    for i, row in enumerate(tasks):
        print(f'{i + 1}. {row.task}. {row.deadline:%d} {row.deadline:%b}')
    print(NEW_LINE)


def add_task():
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


def missed_tasks():
    tasks = database.session.query(database.ToDo).filter(database.ToDo.deadline < datetime.today().date()).all()
    print(NEW_LINE)
    if len(tasks) == 0:
        print("Missed tasks:\nAll tasks have been completed!")
    for i, row in enumerate(tasks):
        print(f"{i + 1}. {row.task}. {row.deadline:%d} {row.deadline:%b}")
    print(NEW_LINE)


def delete_task():
    print(NEW_LINE)
    current_tasks = database.session.query(database.ToDo).order_by(database.ToDo.deadline).all()
    if len(current_tasks) == 0:
        print("Nothing to delete")
        return
    print("Choose the number of the task you want to delete:")
    for i, row in enumerate(current_tasks):
        print(f"{i + 1}. {row.task}. {row.deadline:%d} {row.deadline:%b}")
    while True:
        try:
            task_to_delete = int(input())
        except ValueError:
            print("Invalid input!")
        else:
            if 0 < task_to_delete <= len(current_tasks):
                database.session.delete(current_tasks[task_to_delete - 1])
                database.session.commit()
                print("The task has been deleted!")
                break
            else:
                print("Invalid input!")
    print(NEW_LINE)

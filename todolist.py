import database


def main():
    while True:
        ask_task = input("1) Today's tasks\n2) Add a task\n0) Exit\n")
        match ask_task:
            case "1":
                rows = db.query_db()
                if len(rows) == 0:
                    print("Nothing to do!")
                for i, row in enumerate(rows):
                    print(f'{i + 1}. {row.task}')
                print()
            case "2":
                new_task = input("Enter task\n")
                if new_task:
                    print(db.add_task(new_task))
                else:
                    print("The task has not been added!")
            case "0":
                print("Bye!")
                break


if __name__ == '__main__':
    db = database.ToDo()
    database.main()
    main()

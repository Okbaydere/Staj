from database import *


def login_menu():
    print("""
    Choose an option:
    1- Log In
    2- Sign Up
    3- Exit
    """)


def task_menu():
    print("""
    1-Create Task and Assign Points
    2-List by Date
    3-List by Points
    4-View Task IDs
    5-Delete Task
    6-Back to Main Menu
    """)


def add_data():
    username = input("Create a username:")
    password = input("Create a password:")
    add_user_data(username, password)


def task_list(select_task):
    if select_task == 1:
        task = input("Enter the task you want to create:")
        task_point = int(input("Enter the points for the task you created:"))
        add_task_data(task, task_point, username)

    elif select_task == 2:
        list_by_date(control[0])
    elif select_task == 3:
        list_by_point(control[0])
    elif select_task == 4:
        show_id(control[0])
    elif select_task == 5:
        delete = int(input("Enter the ID of the task you want to delete:"))
        delete_task(delete)


while True:
    login_menu()
    try:
        select = int(input("Choose an option:"))
        if select == 1:
            username = input("Username:")
            password = input("Password:")
            control = is_user_exist(username)
            if control is None:
                print("User does not exist")
                continue
            if password == control[2]:
                while True:
                    task_menu()
                    try:
                        select_task = int(input("Choose an option:"))
                        task_list(select_task)
                        if select_task == 6:
                            break
                    except ValueError:
                        print("Please enter a number")
            elif password != control[2]:
                print("Incorrect Password")

        if select == 2:
            add_data()
        if select == 3:
            break

    except ValueError:
        print("Please enter a number")

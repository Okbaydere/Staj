import sqlite3 as sql

con = sql.connect('tasklist.db')
con.execute("PRAGMA foreign_keys = 1")
cursor = con.cursor()

def create_table():
    cursor.execute \
        ("CREATE TABLE IF NOT EXISTS member "
         "(Id INTEGER PRIMARY KEY ,"
         "user_name TEXT,"
         "user_password TEXT,"
         "UNIQUE (user_name))")
    cursor.execute \
        ("CREATE TABLE IF NOT EXISTS "
         "task ("
         "Id INTEGER PRIMARY KEY AUTOINCREMENT , "
         "user_id INTEGER,"
         "task_name TEXT,"
         "task_point INTEGER,"
         "task_date DATE ,"
         "FOREIGN KEY (user_id) REFERENCES member(Id))")
    con.commit()

create_table()

def add_user_data(user_name, user_password):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()
    try:
        add = "INSERT INTO member(user_name, user_password) VALUES ('{}','{}') "
        cursor.execute(add.format(user_name, user_password))
        con.commit()
    except:
        print("A member with the same name already exists!")

    con.close()

def add_task_data(task_name, task_point, member):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()
    idg = is_user_exist(member)

    add = "INSERT INTO task(task_name, task_point,task_date,user_id)  VALUES ('{}','{}',datetime(),'{}') "
    cursor.execute(add.format(task_name, task_point, idg[0]))
    con.commit()
    con.close()

def delete_task(task_Id):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()
    delete = "DELETE FROM task WHERE Id = '{}' "
    cursor.execute(delete.format(task_Id))
    con.commit()
    con.close()

def is_user_exist(user_name):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()
    search = "SELECT * FROM member WHERE user_name = '{}'"
    cursor.execute(search.format(user_name))
    user = cursor.fetchone()
    con.close()
    return user

def list_by_point(control):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()

    listing = "SELECT task_name,task_point FROM task WHERE user_id = '{}' ORDER BY task_point"
    cursor.execute(listing.format(control))
    lbp = cursor.fetchall()  # list by point
    for i in lbp:
        print(i)
    con.close()

def list_by_date(control):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()

    listing = "SELECT task_name,task_date FROM task WHERE user_id = '{}' ORDER BY datetime()"
    cursor.execute(listing.format(control))
    lbd = cursor.fetchall()  # list by date
    for i in lbd:
        print(i)
    con.close()

def show_id(control):
    con = sql.connect('tasklist.db')
    cursor = con.cursor()

    listing = "SELECT Id,task_name FROM task WHERE user_id = '{}'"
    cursor.execute(listing.format(control))
    lbi = cursor.fetchall()  # list by ID
    for i in lbi:
        print(i)
    con.close()

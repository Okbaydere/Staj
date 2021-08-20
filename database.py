import sqlite3 as sql

con = sql.connect('gorevlistesi.db')
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
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    try:
        add = "INSERT INTO member(user_name, user_password) VALUES ('{}','{}') "
        cursor.execute(add.format(user_name, user_password))
        con.commit()
    except:
        print("Aynı isimde farklı bir üye var!")

    con.close()


def add_task_data(task_name, task_point, member):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    idg = get_id_user(member)
    add = "INSERT INTO task(task_name, task_point,task_date,user_id)  VALUES ('{}','{}',datetime(),'{}') "
    cursor.execute(add.format(task_name, task_point, idg[0]))
    con.commit()
    con.close()


def delete_task(task_Id):  # Görev Sil
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    delete = "DELETE FROM task WHERE Id = '{}' "
    cursor.execute(delete.format(task_Id))
    con.commit()
    con.close()


def is_user_exist(user_name):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    search = "SELECT * FROM member WHERE user_name = '{}'"
    cursor.execute(search.format(user_name))
    user = cursor.fetchone()
    con.close()
    return user


def list_by_point():
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()

    cursor.execute("SELECT task_name,task_point FROM task ORDER BY task_point")
    listing = cursor.fetchall()
    for i in listing:
        print(i)
    con.close()


def list_by_date():
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    cursor.execute("SELECT task_name,task_date  FROM task ORDER BY task_date")
    listing = cursor.fetchall()
    for i in listing:
        print(i)
    con.close()


def get_id_user(user_name):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    get = "SELECT Id FROM member WHERE user_name = '{}' LIMIT 1"
    cursor.execute(get.format(user_name))
    user_id = cursor.fetchone()
    con.close()
    return user_id

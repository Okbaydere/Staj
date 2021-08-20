import sqlite3 as sql

con = sql.connect('gorevlistesi.db')
con.execute("PRAGMA foreign_keys = 1")
cursor = con.cursor()


def create_table():
    cursor.execute \
        ("CREATE TABLE IF NOT EXISTS member "
         "(Id INTEGER PRIMARY KEY ,"
         "userName TEXT,"
         "userPassword TEXT,"
         "UNIQUE (userName))")
    cursor.execute \
        ("CREATE TABLE IF NOT EXISTS "
         "task ("
         "Id INTEGER PRIMARY KEY AUTOINCREMENT , "
         "userid INTEGER,"
         "taskName TEXT,"
         "taskPoint INTEGER,"
         "taskDate DATE ,"
         "FOREIGN KEY (userid) REFERENCES member(Id))")
    con.commit()


create_table()


def add_user_data(userName, userPassword):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    try:
        ekle = "INSERT INTO member(userName, userPassword) VALUES ('{}','{}') "
        cursor.execute(ekle.format(userName, userPassword))
        con.commit()
    except:
        print("Aynı isimde farklı bir üye var!")

    con.close()


def add_task_data(taskName, taskPoint, member):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    idg = getid(member)
    ekle = "INSERT INTO task(taskName, taskPoint,taskDate,userid)  VALUES ('{}','{}',datetime(),'{}') "
    cursor.execute(ekle.format(taskName, taskPoint, idg[0]))
    con.commit()
    con.close()


def deletetask(taskName):  # Görev Sil
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    sil = "DELETE FROM task WHERE taskName = '{}' "
    cursor.execute(sil.format(taskName))
    con.commit()
    con.close()


def isuserexist(userName):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    arama = "SELECT * FROM member WHERE userName = '{}'"
    cursor.execute(arama.format(userName))
    user = cursor.fetchone()
    con.close()
    return user


def listbypoint():
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()

    cursor.execute("SELECT taskName,taskPoint FROM task ORDER BY taskPoint")
    listele = cursor.fetchall()
    for i in listele:
        print(i)
    con.close()


def listbydate():
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    cursor.execute("SELECT taskName,taskDate  FROM task ORDER BY taskDate")
    listele = cursor.fetchall()
    for i in listele:
        print(i)
    con.close()


def getid(userName):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    get = "SELECT Id FROM member WHERE userName = '{}' LIMIT 1"
    cursor.execute(get.format(userName))
    userid = cursor.fetchone()
    con.close()
    return userid

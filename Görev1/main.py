from database import *


def login_menu():
    print("""
    Bir seçim yapınız
    1- Giriş Yap
    2- Üye Ol
    3- Çıkış yap
    """)


def task_menu():
    print("""
    1-Görev Olustur ve puan Ver
    2-Tarihe göre listele
    3-Puana göre listele
    4-Görevlerin ID'sini gör
    5-Görev sil
    6-Ana menüye dön
    """)


def add_data():
    username = input("Kullanıcı adı oluştur:")
    password = input("Şifre oluştur:")
    add_user_data(username, password)


def task_list(select_task):
    if select_task == 1:
        task = input("Oluşturmak istediğiniz görevi giriniz:")
        task_point = int(input("Oluşturduğunuz görevin puanını giriniz:"))
        add_task_data(task, task_point, username)


    elif select_task == 2:
        list_by_date(control[0])
    elif select_task == 3:
        list_by_point(control[0])
    elif select_task == 4:
        show_id(control[0])
    elif select_task == 5:
        delete = int(input("Silmek istediğiniz görevin ID'sini giriniz:"))
        delete_task(delete)


while True:

    login_menu()
    try:
        select = int(input("Bir seçim yapınız:"))
        if select == 1:
            username = input("Kullanıcı adı:")
            password = input("Şifre:")
            control = is_user_exist(username)
            if control is None:
                print("Böyle bir kullanıcı yok")
                continue
            if password == control[2]:
                while True:
                    task_menu()
                    try:
                        select_task = int(input("Bir seçim yapınız:"))
                        task_list(select_task)
                        if select_task == 6:
                            break
                    except ValueError:
                        print("Lütfen rakam giriniz")
            elif password != control[2]:
                print("Şifre Hatalı")

        if select == 2:
            add_data()
        if select == 3:
            break


    except ValueError:
        print("Lütfen rakam girin")

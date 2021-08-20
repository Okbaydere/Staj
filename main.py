from database import *


def login():
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
    4-Görev delete
    5-Ana menüye dön
    """)


while True:

    login()
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
                        if select_task == 1:
                            task = input("Oluşturmak istediğiniz görevi giriniz:")
                            task_point = input("Oluşturduğunuz görevin puanını giriniz:")

                            add_task_data(task, task_point, username)
                        elif select_task == 2:
                            list_by_date()
                        elif select_task == 3:
                            list_by_date()
                        elif select_task == 4:
                            delete = input("Silmek istediğiniz görevin tam adını giriniz:")
                            delete_task(delete)
                        elif select_task == 5:
                            break

                    except ValueError:
                        print("Lütfen rakam giriniz")
            else:
                print("Şifre Hatalı")

        if select == 2:
            username = input("Kullanıcı adı oluştur:")
            password = input("Şifre oluştur:")
            add_user_data(username, password)
        if select == 3:
            break

    except ValueError:
        print("Rakam gir")

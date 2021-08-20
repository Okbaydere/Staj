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
    4-Görev Sil
    5-Ana menüye dön
    """)


while True:

    login()
    try:
        select = int(input("Bir seçim yapınız:"))
        if select == 1:
            username = input("Kullanıcı adı:")
            password = input("Şifre:")
            kontrol = isuserexist(username)
            if kontrol is None:
                print("Böyle bir kullanıcı yok")
                continue
            if password == kontrol[2]:
                while True:
                    task_menu()
                    try:

                        selecttask = int(input("Bir seçim yapınız:"))
                        if selecttask == 1:
                            task = input("Oluşturmak istediğiniz görevi giriniz:")
                            taskpoint = input("Oluşturduğunuz görevin puanını giriniz:")

                            add_task_data(task, taskpoint, username)
                        elif selecttask == 2:
                            listbydate()
                        elif selecttask == 3:
                            listbydate()
                        elif selecttask == 4:
                            sil = input("Silmek istediğiniz görevin tam adını giriniz:")
                            deletetask(sil)
                        elif selecttask == 5:
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

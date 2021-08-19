from database import *


def login():
    print("""
    Bir seçim yapınız
    1- Giriş Yap
    2- Üye Ol
    3- Çıkış yap
    """)


def taskmenu():
    print("""
    1-Görev Olustur ve Puan Ver
    2-Tarihe göre listele
    3-Puana göre listele
    4-Görev Sil
    5-Ana menüye dön
    """)


while True:

    login()
    try:
        secim = int(input("Bir seçim yapınız:"))
        if secim == 1:
            kullaniciAdi = input("Kullanıcı adı:")
            Sifre = input("Sifre:")
            kontrol = KullaniciVarMi(kullaniciAdi)
            if kontrol is None:
                print("Böyle bir kullanıcı yok")
                continue
            if Sifre == kontrol[2]:
                while True:
                    taskmenu()
                    try:

                        gorevSecim = int(input("Bir seçim yapınız:"))
                        if gorevSecim == 1:
                            gorev = input("Oluşturmak istediğiniz görevi giriniz:")
                            gorevPuani = input("Oluşturduğunuz görevin puanını giriniz:")
                            Uye = kullaniciAdi
                            GorevVeriEkle(gorev, gorevPuani, Uye)
                        elif gorevSecim == 2:
                            TariheGoreListele()
                        elif gorevSecim == 3:
                            PuanaGoreListele()
                        elif gorevSecim == 4:
                            sil = input("Silmek istediğiniz görevin tam adını giriniz:")
                        elif gorevSecim == 5:
                            break

                    except ValueError:
                        print("Lütfen rakam giriniz")
            else:
                print("Şifre Hatalı")

        if secim == 2:
            kullaniciAdi = input("Kullanıcı adı oluştur:")
            Sifre = input("Şifre oluştur:")
            UyeVeriEkle(kullaniciAdi, Sifre)
            print("Kayıt oluşturuldu")
        if secim == 3:
            break
        else:
            print("Üstteki rakamlardan giriniz lütfen")
    except ValueError:
        print("Rakam gir")

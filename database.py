import sqlite3 as sql

con = sql.connect('gorevlistesi.db')
con.execute("PRAGMA foreign_keys = 1")
cursor = con.cursor()


def tabloolustur():
    cursor.execute \
        ("CREATE TABLE IF NOT EXISTS uye "
         "(Id INTEGER PRIMARY KEY ,"
         "UyeAdi TEXT,"
         "UyeSifre TEXT )")
    cursor.execute \
        ("CREATE TABLE IF NOT EXISTS "
         "gorev ("
         "Id INTEGER PRIMARY KEY AUTOINCREMENT , "
         "UyeId INTEGER,"
         "gorevAdi TEXT,"
         "gorevPuani INTEGER,"
         "gorevTarihi DATE ,"
         "FOREIGN KEY (UyeId) REFERENCES uye(Id))")
    con.commit()


tabloolustur()


def UyeVeriEkle(UyeAdi, UyeSifre):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    ekle = "INSERT INTO uye(UyeAdi, UyeSifre) VALUES ('{}','{}') "
    cursor.execute(ekle.format(UyeAdi, UyeSifre))
    con.commit()
    con.close()


def GorevVeriEkle(gorevAdi, gorevPuani, Uye):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    IdG = IdGetir(Uye)
    ekle = "INSERT INTO gorev(gorevAdi, gorevPuani,gorevTarihi,UyeId)  VALUES ('{}','{}',datetime(),'{}') "
    cursor.execute(ekle.format(gorevAdi, gorevPuani, IdG[0]))
    con.commit()
    con.close()


def GorevSil(gorevAdi):  # Görev Sil
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    sil = "DELETE FROM gorev WHERE gorevAdi = '{}' "
    cursor.execute(sil.format(gorevAdi))
    con.commit()
    con.close()


def KullaniciVarMi(UyeAdi):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    arama = "SELECT * FROM uye WHERE UyeAdi = '{}'"
    cursor.execute(arama.format(UyeAdi))
    kullanici = cursor.fetchone()
    con.close()
    return kullanici


def PuanaGoreListele():
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()

    cursor.execute("SELECT gorevAdi,gorevPuani FROM gorev WHERE UyeId=1  ORDER BY gorevPuani")
    listele = cursor.fetchall()
    for i in listele:
        print(i)
    con.close()


def TariheGoreListele():
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    cursor.execute("SELECT gorevAdi,gorevTarihi  FROM gorev WHERE UyeId=1 ORDER BY gorevTarihi")
    listele = cursor.fetchall()
    for i in listele:
        print(i)
    con.close()


def IdGetir(UyeAdi):
    con = sql.connect('gorevlistesi.db')
    cursor = con.cursor()
    getir = "SELECT Id FROM uye WHERE UyeAdi = '{}' LIMIT 1"
    cursor.execute(getir.format(UyeAdi))
    KullaniciId = cursor.fetchone()
    con.close()
    return KullaniciId


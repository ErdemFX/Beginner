import sqlite3
import sys
import time

vt = sqlite3.connect('C:/Users/Erdem/Desktop/dizikafesi.sqlite')
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS personel (isim, soyisim, memleket, telno)")


isim = input("Lütfen veritabanına işlenmesi gereken ismi girin: ")
soyisim = input("Lütfen veritabanına işlenmesi gereken soyismi girin: ")
memleket = input("Lütfen veritabanına işlenmesi gereken memleketi girin: ")
telno = input("Lütfen veritabanına işlenmesi gereken telefon numarasını girin: ")
#print(f"İşlem başarılı! Girilen veriler: \n İsim: {isim} \nSoyisim: {soyisim} \n Memleket: {memleket} \nTelefon numarası: {telno}")

params = (isim, soyisim, memleket, telno)

im.execute("INSERT INTO personel (isim, soyisim, memleket, telno) VALUES (?, ?, ?, ?)", params)
vt.commit()
im.execute("SELECT * FROM personel")
vtverileri = im.fetchall()

time.sleep(2)
evh = input("Güncel veri tabanı durumunu görüntülemek istiyor musunuz? (Evet/Hayır) : ")
evh = evh.lower()
if evh == "evet":
    time.sleep(1)
    print(f"Güncel veritabanı verileri: {vtverileri}")
    sys.exit()
if evh == "hayır":
    time.sleep(1)
    print("Anlaşıldı patron. Kapatıyoruz dükkanı.")
    sys.exit()


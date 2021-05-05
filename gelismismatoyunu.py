#### IMPORT START ####
import random
import os
import getpass
import sys
import time
import sqlite3
#### IMPORT END ####

path = getpass.getuser()

#### DATABASE START ####
os.chdir('C:/Users/'+path+'/Documents')
if os.path.exists('Matoyunu'):
    print("Veritabanı yolu başarıyla tespit edildi.")
    time.sleep(1)
else:
    os.mkdir('Matoyunu')
    print("Veritabanı yolu başarıyla oluşturuldu!")
    time.sleep(1)
db = sqlite3.connect("C:/Users/"+path+"/Documents/Matoyunu/matoyunu.db")
im = db.cursor()
im.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullanici_adi, parola)")
kullanicilar = [("root", "root")]
for i in kullanicilar:
    im.execute("""INSERT INTO kullanicilar VALUES (?, ?)""", i)
db.commit()
kull = input("Kullanıcı adınız: ")
print("-" * len(str("Kullanıcı adınız: ")))
parola = input("Parolanızı girin: ")
print("-" * len(str("Parolanızı girin: ")))
im.execute("""SELECT * FROM kullanicilar WHERE kullanici_adi = ? AND parola = ?""", (kull, parola))

#### DATABASE END ####

#### USER CHECK AND GAME START ####

data = im.fetchone()

if data:
    time.sleep(0.5)
    print("Giriş başarılı! \n \nOyuna yönlendiriliyorsunuz...")
    print("-" * len(str("Giriş başarılı! \n \nOyuna yönlendiriliyorsunuz...")))
    time.sleep(1)
    class MatOyunu(object):
        def __init__(self):
            self.sayi1 = random.randint(1, 9)
            self.sayi2 = random.randint(1, 9)
            self.sayi3 = random.randint(150, 300)
            self.sayi4 = random.randint(1, 150)
            self.sayi5 = random.randint(1, 300)
            self.sayi6 = random.randint(1, 300)
            self.puan = 100

        def Secenek(self, secim=6):
            self.secim = secim
            print("")
            print("Çarpım Tablosu Oyunu için 1'e basınız.")
            print("-" * len(str("Çarpım Tablosu Oyunu için 1'e basınız.")))
            print("Toplama Oyunu için 2'ye basınız.")
            print("-" * len(str("Toplama Oyunu için 2'ye basınız.")))
            print("Çıkarma Oyunu için 3'e basınız.")
            print("-" * len(str("Çıkarma Oyunu için 3'e basınız.")))
            print(f"Güncel puanın: {self.puan}")
            print("-" * len(str(f"Güncel puanın: {self.puan}")))
            while self.secim == 6:
                try:
                    print("")
                    self.secenek = input("Lütfen oynamak istediğiniz oyuna karşılık gelen sayıyı giriniz: ")
                    self.secenek = int(self.secenek)
                    time.sleep(1)
                    print(f"Bilgilendirme! Güncel puanın {self.puan}. Bildiğin her soru için 30 puan kazanacaksın.\nKaybettiğin her soru için 20 puan kaybedeceksin.")
                    while self.secenek == 1:
                        self.sayi1 = random.randint(1, 9)
                        self.sayi2 = random.randint(1, 9)
                        oyunsorusu1 = self.sayi1 * self.sayi2
                        print("")
                        cevap1 = int(input(f"{self.sayi1} ve {self.sayi2} sayılarının çarpımı nedir? (Oyunu kapatmak için 0 yazınız.) \nCevabı giriniz: "))
                        if cevap1 == oyunsorusu1:
                            self.puan = self.puan + 30
                            print("")
                            time.sleep(0.6)
                            print(f"Tebrikler başardınız. Puanınıza 30 puan eklendi!\nGüncel puan {self.puan} \n Yeni soru geliyor...")
                            continue
                        elif cevap1 == 0:
                            print("")
                            print("Oyun kapatılıyor...")
                            time.sleep(1)
                            break
                        else:
                            print("")
                            self.puan = self.puan - 20
                            print(f"Gerçekten bu sorunun cevabını bilemeyecek kadar bilgisiz misin? :(\n 20 Puan kaybettin! \nGüncel puanın {self.puan}")
                    if self.secenek == 2:
                        self.sayi3 = random.randint(150, 300)
                        self.sayi4 = random.randint(1, 150)
                        oyunsorusu2 = self.sayi3 + self.sayi4
                        print("")
                        cevap2 = int(input(f"{self.sayi3} ve {self.sayi4} sayılarının toplamı nedir? (Oyunu kapatmak için 0 yazınız.) \nCevabı giriniz: "))
                        if cevap2 == oyunsorusu2:
                            time.sleep(0.7)
                            print("")
                            self.puan = self.puan + 30
                            print(f"Tebrikler başardınız. \n30 Puan kazandınız! Güncel puanın: {self.puan} \nAna menüye dönülüyor.")
                            print()
                        elif cevap2 == 0:
                            print("")
                            print("Oyun kapatılıyor...")
                            time.sleep(1)
                            break
                        else:
                            time.sleep(0.7)
                            print("")
                            self.puan = self.puan - 20
                            print(f"Gerçekten bu sorunun cevabını bilemeyecek kadar bilgisiz misin? :(\n 20 Puan kaybettin! \nGüncel puanın {self.puan}")
                    if self.secenek == 3:
                        self.sayi5 = random.randint(1, 300)
                        self.sayi6 = random.randint(1, 300)
                        oyunsorusu3 = self.sayi5 + self.sayi6
                        print("")
                        cevap3 = int(input(f"{self.sayi5} ve {self.sayi6} sayılarını çıkarırsak kaç kalır? (Oyunu kapatmak için 0 yazınız.) \nCevabı giriniz: "))
                        if cevap3 == oyunsorusu3:
                            self.puan = self.puan + 30
                            print("")
                            time.sleep(0.7)
                            print(
                                f"Tebrikler başardınız. Puanınıza 30 puan eklendi!\nGüncel puan {self.puan} \n Yeni soru geliyor...")
                        elif cevap3 == 0:
                            print("")
                            print("Oyun kapatılıyor...")
                            time.sleep(1)
                            break
                        else:
                            time.sleep(0.7)
                            print("")
                            self.puan = self.puan - 20
                            print(f"Gerçekten bu sorunun cevabını bilemeyecek kadar bilgisiz misin? :(\n 20 Puan kaybettin! \nGüncel puanın {self.puan}")

                except ValueError:
                    time.sleep(0.7)
                    print("")
                    print("Lütfen sadece oynamak istediğiniz oyunun sayısını giriniz!")
                    time.sleep(2)
                    continue


    oyun = MatOyunu()
    oyun.Secenek()

else:
    time.sleep(1)
    print("Kullanıcı adın veya parolan yanlış! \nÇıkış yapılıyor...")
    sys.exit()

#### USER CHECK AND GAME END ####

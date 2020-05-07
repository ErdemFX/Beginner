import random
import time

class MatOyunu(object):
    def __init__(self):
        self.sayi1 = random.randint(1, 9)
        self.sayi2 = random.randint(1, 9)
        self.sayi3 = random.randint(150, 300)
        self.sayi4 = random.randint(1, 150)
        self.sayi5 = random.randint(1, 300)
        self.sayi6 = random.randint(1, 300)

    def Secenek(self, secim=6):
        self.secim = secim
        print("")
        print("Çarpım Tablosu Oyunu için 1'e basınız.")
        print("-" * len(str("Çarpım Tablosu Oyunu için 1'e basınız.")))
        print("Toplama Oyunu için 2'ye basınız.")
        print("-" * len(str("Toplama Oyunu için 2'ye basınız.")))
        print("Çıkarma Oyunu için 3'e basınız.")
        print("-" * len(str("Çıkarma Oyunu için 3'e basınız.")))
        while self.secim == 6:
            try:
                print("")
                self.secenek = input("Lütfen oynamak istediğiniz oyuna karşılık gelen sayıyı giriniz: ")
                self.secenek = int(self.secenek)
                time.sleep(1)
                while self.secenek == 1:
                    self.sayi1 = random.randint(1, 9)
                    self.sayi2 = random.randint(1, 9)
                    oyunsorusu1 = self.sayi1 * self.sayi2
                    print("")
                    cevap1 = int(input(f"{self.sayi1} ve {self.sayi2} sayılarının çarpımı nedir? (Oyunu kapatmak için 0 yazınız.) \nCevabı giriniz: "))
                    if cevap1 == oyunsorusu1:
                        print("")
                        time.sleep(0.6)
                        print("Tebrikler başardınız. Yeni soru geliyor!!")
                        continue
                    elif cevap1 == 0:
                        print("")
                        print("Oyun kapatılıyor...")
                        time.sleep(1)
                        break
                    else:
                        print("")
                        print("Gerçekten bu sorunun cevabını bilemeyecek kadar bilgisiz misin? :(")
                if self.secenek == 2:
                    self.sayi3 = random.randint(150, 300)
                    self.sayi4 = random.randint(1, 150)
                    oyunsorusu2 = self.sayi3 + self.sayi4
                    print("")
                    cevap2 = int(input(f"{self.sayi3} ve {self.sayi4} sayılarının toplamı nedir? (Oyunu kapatmak için 0 yazınız.) \nCevabı giriniz: "))
                    if cevap2 == oyunsorusu2:
                        time.sleep(0.7)
                        print("")
                        print("Tebrikler başardınız. Ana menüye dönülüyor.")
                    elif cevap2 == 0:
                        print("")
                        print("Oyun kapatılıyor...")
                        time.sleep(1)
                        break
                    else:
                        time.sleep(0.7)
                        print("")
                        print("Gerçekten bu sorunun cevabını bilemeyecek kadar bilgisiz misin? :(")
                if self.secenek == 3:
                    self.sayi5 = random.randint(1, 300)
                    self.sayi6 = random.randint(1, 300)
                    oyunsorusu3 = self.sayi5 + self.sayi6
                    print("")
                    cevap3 = int(input(f"{self.sayi5} ve {self.sayi6} sayılarını çıkarırsak kaç kalır? (Oyunu kapatmak için 0 yazınız.) \nCevabı giriniz: "))
                    if cevap3 == oyunsorusu3:
                        time.sleep(0.7)
                        print("")
                        print("Tebrikler başardınız. Yeni soru geliyor!!")
                    elif cevap3 == 0:
                        print("")
                        print("Oyun kapatılıyor...")
                        time.sleep(1)
                        break
                    else:
                        time.sleep(0.7)
                        print("")
                        print("Gerçekten bu sorunun cevabını bilemeyecek kadar bilgisiz misin? :(")

            except ValueError:
                time.sleep(0.7)
                print("")
                print("Lütfen sadece oynamak istediğiniz oyunun sayısını giriniz!")
                time.sleep(2)
                continue


oyun = MatOyunu()
oyun.Secenek()

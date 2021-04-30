import random
import time


class Oyun(object):
    def __init__(self):
        self.puan = 100

    def Baslat(self, secim=6):
        self.secim = secim
        isim = input(str("Size nasıl hitap etmemi istersiniz: "))
        isim = isim.lower()
        isim = isim.capitalize()
        print("")
        print("Merhaba", isim, "oyunumuza hoş geldin.")
        print("")
        time.sleep(3)
        print("Senden 1 ve 9 arasında bir sayı tahmin etmeni isteyeceğim.")
        print("")
        time.sleep(3)
        print("Şu anda 100 puana sahipsin. Her yanlış tahmin ettiğin sayı için 20 puan kaybedeceksin.")
        time.sleep(3)
        print("")
        print("Her doğru bildiğin sayı için 30 puan kazanacaksın.")
        time.sleep(3)
        print("")
        deim = input(str("Oyuna devam etmek istiyor musun? (Evet/Hayır) :"))
        deim = deim.lower()
        time.sleep(2)
        print("")
        print("Evet başlıyoruz bakalım!")
        while deim == "evet":
            if self.puan > 19:
                self.sayi1 = random.randint(1, 9)
                print("")
                time.sleep(2)
                print("-------------------------------------------------------")
                print("")
                print(f"Güncel puanın: {self.puan}")
                soru = int(input("Aklımdan senin için bir sayı tuttum. Tahmin et bakalım: "))
                if soru == self.sayi1:
                    self.puan = self.puan + 30
                    time.sleep(1)
                    print("-------------------------------------------------------")
                    print(f"Tebrikler! aklımı okudun resmen. Güncel puanın: {self.puan}")
                    print("-------------------------------------------------------")
                    time.sleep(1)
                    print("Yeni soru gelmesi için puanınız kontrol ediliyor...")
                else:
                    self.puan = self.puan - 20
                    time.sleep(1)
                    print("")
                    print(f"Üzgünüm. Aklımdaki sayıyı bulamadın. Güncel puanın: {self.puan}")
                    print("-------------------------------------------------------")
                    time.sleep(1)
                    print("")
                    print("Yeni soru gelmesi için puanınız kontrol ediliyor...")

            else:
                time.sleep(1)
                print("")
                print("Puanınız 20'den az! Oyun kapatılacak...")
                print("")
                time.sleep(1)
                print("Oyun kapatılıyor... (3)")
                print("")
                time.sleep(1)
                print("Oyun kapatılıyor... (2)")
                print("")
                time.sleep(1)
                print("Oyun kapatılıyor... (1)")
                time.sleep(2)
                print("")
                print(f"Üzgünüm {isim} daha sonra görüşürüz :(")
                time.sleep(2)
                exit()
        while deim == "hayır":
            time.sleep(1)
            print("Oyun kapatılıyor... (3)")
            time.sleep(1)
            print("Oyun kapatılıyor... (2)")
            time.sleep(1)
            print("Oyun kapatılıyor... (1)")
            print("")
            time.sleep(2)
            print(f"Üzgünüm {isim} daha sonra görüşürüz :(")
            break


oyun = Oyun()
oyun.Baslat()

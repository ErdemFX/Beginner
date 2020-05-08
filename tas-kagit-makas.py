import random
import time


class TasKagitMakas(object):
    def __init__(self, hazir=0, birdaha=0, senben=0, isim=0, pc_cevabi=2, evet=0, hayir=0):
        self.hazir = hazir
        self.birdaha = birdaha
        self.senben = senben
        self.isim = isim
        self.pc_cevabi = pc_cevabi
        self.evet = evet
        self.hayir = hayir

    def TsKgtMks(self):
        print("\nOyunumuza hoş geldin!\n")
        time.sleep(1)
        self.isim = input("Oyunda size nasıl hitap etmemi istersiniz?\n\nLütfen girin: ")
        self.isim = self.isim.title()
        time.sleep(1)
        print(f"\nMerhaba {self.isim}, oyunumuza tekrardan hoş geldin!\n")
        time.sleep(2)
        self.hazir = input(f"{self.isim}, hazırsan taş kağıt makas oyunumuza başlayalım? \n\nCevabın (e/h): ")
        self.evet = "e"
        self.hayir = "h"
        if not self.hazir == self.evet:
            if not self.hazir == self.hayir:
                time.sleep(1)
                print("\nLütfen sadece istenilen verileri gir!")
                time.sleep(1)
                print("\nSeni cezalandırıyorum ve oyunu kapatıyorum...")
        while self.hazir == self.evet:
            try:
                self.pc_cevabi = random.randint(1, 3)
                if self.pc_cevabi == 1:
                    time.sleep(1)
                    print("\nÜçten geriye doğru sayacağım ve aynı anda söyleyeceğiz!")
                    time.sleep(3)
                    print("\nÜç")
                    time.sleep(1)
                    print("\nİki")
                    time.sleep(1)
                    print("\nBir")
                    time.sleep(1)
                    print("\nTaş!")
                    time.sleep(2.4)
                    self.senben = input("\nKim kazandı? (sen/ben) : ")
                    if self.senben == "sen":
                        time.sleep(1)
                        print("\nGerçekten bir bilgisayara yenilecek kadar düştün mü? :(")
                        time.sleep(3)
                        self.birdaha = input("\nBir daha oynamak ister misin?\n\nCevabın (e/h): ")
                        if self.birdaha == "e":
                            time.sleep(1)
                            print("\nHırsını alamadın demek öyle mi?")
                            time.sleep(2)
                            print("\nYeniden başlatıyorum oyunu...")
                            time.sleep(2)
                            continue
                        elif self.birdaha == "h":
                            time.sleep(1)
                            print("\nOyun kapatılıyor...")
                            time.sleep(2)
                            break
                    if self.senben == "ben":
                        time.sleep(1)
                        print("\nTebrik ederim! Bu işte çok başarılısın galiba.")
                        time.sleep(3)
                        self.birdaha = input("\nBir daha oynamak ister misin?\n\nCevabın (e/h): ")
                        if self.birdaha == "e":
                            time.sleep(1)
                            print("\nHırsını alamadın demek öyle mi?")
                            time.sleep(2)
                            print("\nYeniden başlatıyorum oyunu...")
                            time.sleep(2)
                            continue
                        elif self.birdaha == "h":
                            time.sleep(1)
                            print("\nOyun kapatılıyor...")
                            time.sleep(2)
                            break

                if self.pc_cevabi == 2:
                    time.sleep(1)
                    print("\nÜçten geriye doğru sayacağım ve aynı anda söyleyeceğiz!")
                    time.sleep(3)
                    print("\nÜç")
                    time.sleep(1)
                    print("\nİki")
                    time.sleep(1)
                    print("\nBir")
                    time.sleep(1)
                    print("\nKağıt!")
                    time.sleep(2.4)
                    self.senben = input("\nKim kazandı? (sen/ben) : ")
                    if self.senben == "sen":
                        time.sleep(1)
                        print("\nGerçekten bir bilgisayara yenilecek kadar düştün mü? :(")
                        time.sleep(3)
                        self.birdaha = input("\nBir daha oynamak ister misin?\n\nCevabın (e/h): ")
                        if self.birdaha == "e":
                            time.sleep(1)
                            print("\nVay demekki yenilmeye doymadın ha?")
                            time.sleep(2)
                            print("\nYeniden başlatıyorum oyunu...")
                            time.sleep(2)
                            continue
                        elif self.birdaha == "h":
                            time.sleep(1)
                            print("\nOyun kapatılıyor...")
                            time.sleep(2)
                            break
                    if self.senben == "ben":
                        time.sleep(1)
                        print("\nTebrik ederim! Bu işte çok başarılısın galiba.")
                        time.sleep(3)
                        self.birdaha = input("\nBir daha oynamak ister misin?\n\nCevabın (e/h): ")
                        if self.birdaha == "e":
                            time.sleep(1)
                            print("\nHırsını alamadın demek öyle mi?")
                            time.sleep(2)
                            print("\nYeniden başlatıyorum oyunu...")
                            time.sleep(2)
                            continue
                        elif self.birdaha == "h":
                            time.sleep(1)
                            print("\nOyun kapatılıyor...")
                            time.sleep(2)
                            break

                if self.pc_cevabi == 3:
                    time.sleep(1)
                    print("\nÜçten geriye doğru sayacağım ve aynı anda söyleyeceğiz!")
                    time.sleep(3)
                    print("\nÜç")
                    time.sleep(1)
                    print("\nİki")
                    time.sleep(1)
                    print("\nBir")
                    time.sleep(1)
                    print("\nMakas!")
                    time.sleep(2.4)
                    self.senben = input("\nKim kazandı? (sen/ben) : ")
                    if self.senben == "sen":
                        time.sleep(1)
                        print("\nGerçekten bir bilgisayara yenilecek kadar düştün mü? :(")
                        time.sleep(3)
                        self.birdaha = input("\nBir daha oynamak ister misin?\n\nCevabın (e/h): ")
                        if self.birdaha == "e" or "evet":
                            time.sleep(1)
                            print("\nVay demekki yenilmeye doymadın ha?")
                            time.sleep(2)
                            print("\nYeniden başlatıyorum oyunu...")
                            time.sleep(2)
                            continue
                        elif self.birdaha == "h" or "hayır":
                            time.sleep(1)
                            print("\nOyun kapatılıyor...")
                            time.sleep(2)
                            break
                    if self.senben == "ben":
                        time.sleep(1)
                        print("\nTebrik ederim! Bu işte çok başarılısın galiba.")
                        time.sleep(3)
                        self.birdaha = input("\nBir daha oynamak ister misin?\n\nCevabın (e/h): ")
                        if self.birdaha == "e":
                            time.sleep(1)
                            print("\nHırsını alamadın demek öyle mi?")
                            time.sleep(2)
                            print("\nYeniden başlatıyorum oyunu...")
                            time.sleep(2)
                            continue
                        if self.birdaha == "h":
                            time.sleep(1)
                            print("\nOyun kapatılıyor...")
                            time.sleep(2)
                            break
                    else:
                        time.sleep(1)
                        print("\nOyun kapatılıyor...")
                        time.sleep(2)
                        break

            except ValueError:
                print("Lütfen sadece istendiği şeyleri girin!")
        while self.hazir == self.hayir:
            try:
                time.sleep(1)
                print("\nOyun kapatılıyor...")
                time.sleep(2)
                break
            except ValueError:
                print("\nError - Lütfen istenilen verileri giriniz!")


taskagitmakas = TasKagitMakas()
taskagitmakas.TsKgtMks()

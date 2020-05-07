class Kedi(object):
    def __init__(self):
        pass
    def yasat(self):
        while True:
            try:
                isim = str(input("Kedinizin ismini giriniz: "))
                kilo = int(input("\nKedinizin kilosunu giriniz: "))
                if kilo < 30:
                    pass
                else:
                    print("\nDostum bu kadar kilolu bir kedi olamaz!")
                    continue
                yas = int(input("\nKedinizin yaşını giriniz: "))
                durum = str(input("\nKedinizin durumunu (sağ/ölü) giriniz: "))
                veritabani = open(f'{isim}.txt','a')
                veritabani.write(f"\nKedinizin ismi: {isim} \nKedinizin kilosu: {kilo}\nKedinizin yaşı: {yas}\nKedinizin durumu: {durum} \n ")
                veritabani.close()
                break

            except ValueError:
                print("  \nLütfen sadece istenilen verileri giriniz. \n  ")
                continue

kedi = Kedi()
kedi.yasat()
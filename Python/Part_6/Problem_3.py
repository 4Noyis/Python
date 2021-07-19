# Proje 3
# Bu projede ise 4 tane sınıfı oluşturun.

# Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

# Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

# Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

# At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.



import time

class Hayvanlar():
    def __init__(self,tur="Omurgalılar ve Omurgasızlar",yasamalanı="Kara, Hava ve Su",beslenmeturu="Etçil, Otçul veya hem etçil hem otçul",ayaksayısı="2-4 arası değişmektedir"):
        self.tur=tur
        self.yasamalanı=yasamalanı
        self.beslenmeturu=beslenmeturu
        self.ayaksayısı=ayaksayısı
    def bilgilerigoster(self):
        print("Türler:{}\nYaşam Alanları:{}\nBeslenme Türleri:{}\nAyak Sayıları:{}\n".format(self.tur,self.yasamalanı,self.beslenmeturu,self.ayaksayısı))


class kopekler(Hayvanlar):
    def __init__(self, tur="Memeli", yasamalanı="Kara", beslenmeturu="Etçil", ayaksayısı="4", cinsleri=["Pitbull","Golden","Rotweiler"]):
        super().__init__(tur=tur, yasamalanı=yasamalanı, beslenmeturu=beslenmeturu, ayaksayısı=ayaksayısı)
        self.cinsleri=cinsleri
    def bilgilerigoster(self):
        print("-KÖPEKLER-")
        print("Tür:{}\nYaşam Alanları:{}\nBeslenme Türü:{}\nAyak Sayısı:{}\nCinsleri:7{}\n".format(self.tur,self.yasamalanı,self.beslenmeturu,self.ayaksayısı,self.cinsleri))
        time.sleep(5)
    def __str__(self) -> str:
        return "Cins Sayısı:{} ".format(len(self.cinsleri))
    def cinsekle(self):
        cins_ismi=input("Cins İsimlerini araya boşluk bırakarak giriniz:")
        cins_listesi=cins_ismi.split("-")
        for i in cins_listesi:
            self.cinsleri.append(i)


class kuslar(Hayvanlar):
    def __init__(self, tur="Omurgalı", yasamalanı="Hava", beslenmeturu="Hem etçil hem otçul", ayaksayısı="2",cinsleri=["Muhabbet Kuşu","Sultan Papağanı","Hint Bülbülü","Amazon Papağanı"]):
        super().__init__(tur=tur, yasamalanı=yasamalanı, beslenmeturu=beslenmeturu, ayaksayısı=ayaksayısı)
        self.cinsleri=cinsleri
    def bilgilerigoster(self):
        print("-KUŞLAR-")
        print("Tür:{}\nYaşam Alanı:{}\nBeslenme Türü:{}\nAyak Sayısı:{}\nCinsleri:{}\n".format(self.tur,self.yasamalanı,self.beslenmeturu,self.ayaksayısı,self.cinsleri))
        time.sleep(5)
    def __str__(self) -> str:
        return "Cins Sayısı:{} ".format(len(self.cinsleri))
    def cinsekle(self):
        cins_ismi=input("Cins İsimlerini araya boşluk bırakarak giriniz:")
        cins_listesi=cins_ismi.split("-")
        for i in cins_listesi:
            self.cinsleri.append(i)

class atlar(Hayvanlar):
    def __init__(self, tur="Memeli", yasamalanı="Kara", beslenmeturu="Hem etçil hem otçul", ayaksayısı="4",cinsleri=["Dole pony","Arap Atı","İngiliz Atı"]):
        super().__init__(tur=tur, yasamalanı=yasamalanı, beslenmeturu=beslenmeturu, ayaksayısı=ayaksayısı)
        self.cinsleri=cinsleri
    def bilgilerigoster(self):
        print("-ATLAR-")
        print("Tür:{}\nYaşam Alanı:{}\nBeslenme Türü:{}\nAyak Sayısı:{}\nCinsleri:{}\n".format(self.tur,self.yasamalanı,self.beslenmeturu,self.ayaksayısı,self.cinsleri))
        time.sleep(5)
    def __str__(self) -> str:
        return "Cinsleri:{} ".format(len(self.cinsleri))
    def cinsekle(self):
        cins_ismi=input("Cins İsimlerini araya '-' bırakarak giriniz:")
        cins_listesi=cins_ismi.split("-")
        for i in cins_listesi:
            self.cinsleri.append(i)

while True:
    print("""
    ---------------------
          Hayvanlar
    ---------------------
    1=Hayvanların Genel Özellikleri
    2=Köpeklerin Genel Özellikleri
    3=Kuşların Genel Özellikleri
    4=Atların Genel Özellikleri
    q=Çıkış

    """)
    işlem=input("İşlem: ")
    if(işlem=="1"):
        hayvanlar=Hayvanlar()
        hayvanlar.bilgilerigoster()
        time.sleep(2)
    elif(işlem=="2"):
        köpekler=kopekler()
        köpekler.bilgilerigoster()
        print("1=Cins Ekle\n2=Cins Sayısı\nb=Geri git\n")
        iş=input("İşlem Seçin: ")
        if(iş=="1"):
            köpekler.cinsekle()
            print(köpekler.cinsleri)
            time.sleep(3)
        elif(iş=="2"):
            print("Cins Sayısı:",köpekler)
            time.sleep(2)
        elif(iş=="b"):
            continue
    elif(işlem=="3"):
        kuşlar=kuslar()
        kuşlar.bilgilerigoster()
        print("1=Cins Ekle\n2=Cins Sayısı\nb=Geri git\n")
        iş=input("İşlem Seçin: ")
        if(iş=="1"):
            kuşlar.cinsekle()
            print(kuşlar.cinsleri)
            time.sleep(3)
        elif(iş=="2"):
            print("Cins Sayısı:",kuşlar)
            time.sleep(2)
        elif(iş=="b"):
            continue
    elif(işlem=="4"):
        at=atlar()
        at.bilgilerigoster()
        print("1=Cins Ekle\n2=Cins Sayısı\nb=Geri git\n")
        iş=input("İşlem Seçin: ")
        if(iş=="1"):
            at.cinsekle()
            print(at.cinsleri)
            time.sleep(3)
        elif(iş=="2"):
            print("Cins Sayısı:",at)
            time.sleep(2)
        elif(iş=="b"):
            continue
    elif(işlem=="q"):
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Geçersiz İşlem...")
        time.sleep(3)
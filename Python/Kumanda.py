import random
import time
class Kumnda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Zaten Açık")
        else:
            print("Tv Açıldı")
            self.tv_durum="Açık"        
    def tv_kapa(self):
        if(self.tv_durum=="Kapalı"):
            print("Zaten Kapalı")
        else:
            print("Tv Kapandı")
            self.tv_durum="Kapalı"
    def ses_ayarları(self):
        while True:
            cevap=input("ses arttırmak için: '>'\nses kısmak için: '<'\nçıkışmak için: 'çıkış\n'")

            if(cevap==">"):
                if(self.tv_ses !=31):
                    self.tv_ses += 1
                    print("ses:",self.tv_ses)
            elif(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses -=1
                    print("ses:",self.tv_ses)
            else:
                print("Çıkış yapıldı\n ses:",self.tv_ses)   
                break             
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durum:{}\ntv ses:{}\nkanal listesi:{}\nkanal:{} ".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)     
    def kanal_ekle(self,kanal_isim):
        print("Kanal Ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_isim)
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        print("Kanal:",self.kanal)   

kumanda = Kumnda()
print("""
1. Tv'yi aç.
2. Tv'yi kapa.
3. Ses Ayarları
4. kanal Listesi
5. Rastgele Kanal
6. Tv Bilgi
7. Kanal Ekle

Çıkış 'q'
""")

while True:
    işlem =input("İşlem:")

    if(işlem=="1"):
        kumanda.tv_ac()
    elif(işlem=="2"):
        kumanda.tv_kapa()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem=="4"):
        len(kumanda)       
    elif(işlem=="5"):
        kumanda.rastgele_kanal()
    elif(işlem=="6"):
        print(kumanda)
    elif(işlem=="7"):
        eklencek_kanal=input("kanal ismi:")
        kumanda.kanal_ekle(eklencek_kanal)

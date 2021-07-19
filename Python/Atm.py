print("""" 
******************************
Atm Programına Hoşgeldiniz

İşlemler;

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için "4" tuşuna basın

*******************************
""")

Bakiye=1000

while True:
    işlem=int(input("İşlem Seçiniz:"))

    if(işlem==1):
        print("Mevcut Bakiye",Bakiye)
    elif(işlem==2):
        miktar=int(input("Yüklenicek Miktarı yazın: "))
        Bakiye +=miktar
        print("Bakiyeiz:",Bakiye)
    elif(işlem==3):
        çek=int(input("Çekmek istediğiniz Miktarı girin: "))
        if(Bakiye-çek>=0):
            Bakiye-=çek
            print("işlem tamamlandı Bakiyeniz: ",Bakiye)
        else:
            print("Hatalı İşlem...")
            continue 
    elif(işlem==4):
        print("Çıkış Yapılıyor..")
        break
    else:
        print("Geçeersiz iŞLEM...")                
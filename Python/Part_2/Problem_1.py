# Problem 1
#Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 #Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 #BKİ 18.5'un altındaysa -------> Zayıf

 #BKİ 18.5 ile 25 arasındaysa ------> Normal

 #BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 #BKİ 30'un üstündeyse -------------> Obez

Kilo= int(input("Kilonuzu Giriniz: "))
Boy= float(input("Boyunuzu Giriniz: "))

KitleIndexi= Kilo / (Boy*Boy)

print("Kütle İndeksiniz:",KitleIndexi)

if(KitleIndexi<18.5):
    print("Zayıfsın.")
elif(18.5<KitleIndexi<25):
    print("Normalsin.")   
elif(25<KitleIndexi<30):
    print("Fazla Kilolusun.")
elif(KitleIndexi>30):
    print("Obezz.")
else:
    print("YANLIŞ DEĞER GİRDİNİZ...")             
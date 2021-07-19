# Proje 1
# Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.

import math

print("""
-------------------------
Hesap Makinesi

1.İşlem: Faktöriyel (factorial)
2.İşlem: 10 tabanında logaritma alır (log10)
3.İşlem: Sayının karekökünün tam sayı değeri (isqrt)
4.İşlem: Sinüs değerini verir (sin)
5.İşlem: Cosinüs değerini verir (cos)
6.İşlem: Tanjant Değerini verir (tan)

Çıkmak için 'q' tuşuna basınız

""")

while True:
    islem=input("İşlem Seçin: ")
    if(islem=="q"):
        print("Çıkış Yapılıyor...")
        break
    if(islem=="1"):
        sayi=int(input("Sayı Girin: "))
        print(math.factorial(sayi))
    elif(islem=="2"):
        sayi=int(input("Sayı Girin: "))
        print("{} 10 tabanında logaritması:{} ".format(sayi,math.log10(sayi)))
    elif(islem=="3"):
        sayi=int(input("Sayı Girin: "))
        print("{} karekökünün tam sayı değeri:{} ".format(sayi,math.isqrt(sayi)))
    elif(islem=="4"):
        sayi=int(input("Sayı Girin: "))
        print("{} sin değeri:{} ".format(sayi,math.sin(sayi)))
    elif(islem=="5"):
        sayi=int(input("Sayı Girin: "))
        print("{} cos değeri:{} ".format(sayi,math.cos(sayi)))
    elif(islem=="6"):
        sayi=int(input("Sayı Girin: "))
        print("{} tanjant değeri:{} ".format(sayi,math.tan(sayi)))  
    else:
        print("Geçersiz İşlem...")
        continue
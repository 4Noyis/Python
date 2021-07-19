print("""
*******************
Faktöriyel Programı
*******************

Çıkmak İçin "q" ya basınız
""")

while True:
    sayı=input("Sayı:")
    if(sayı=="q"):
        print("Çıkış Yapılıyor")
        break
    else:
        sayı=int(sayı)
        faktöriyel=1
        for i in range(2,sayı+1):
            faktöriyel*=i
    print(faktöriyel)
    
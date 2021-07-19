#Problem 4
#Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
#  Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

#İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

print(""" 
*********************************
Toplama Makinnesi

Toplamak istediğiniz sayıyı yazın

Sonucu görmek için 'q' ya basınız
*********************************

""")

Toplam=0

while True:
    sayi=input("Bir Sayı girin: ")
    if(sayi=="q"):
        print("Toplam:",Toplam)
        break
    else:
        sayi=int(sayi)
        Toplam += sayi    

#Problem 4
#Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

#Örnek: 97 ---------> Doksan Yedi

sayi=int(input("sayı:"))

onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

def oku(sayi):
    on=sayi//10
    bir=sayi%10
    return onlar[on],birler[bir]


print(oku(sayi))    

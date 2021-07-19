#Problem 1
#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
# Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).



def perfect(sayi):
    i = 1
    toplam = 0
    while (i < sayi):
        if (sayi % i == 0):
            toplam += i
        i += 1       
    if(toplam==sayi):
        return True
    else:
        return False            

while True:
    sayi=int(input("sayı:"))

    if(perfect(sayi)==True):
        print(sayi,"perfect")
    else:
        print("not perfect")            
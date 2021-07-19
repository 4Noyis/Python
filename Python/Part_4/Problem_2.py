#Problem 2
#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.


liste1=list()
liste2=list()
def ebob1(sayi1):
    for i in range(1,sayi1):
        if(sayi1%i==0):
            liste1.append(i)
    return True       

def ebob2(sayi2):
    for i in range(1,sayi2):
        if(sayi2%i==0):
            liste2.append(i)
    return True


while True:
    sayi1=int(input("sayı1:"))
    sayi2=int(input("Sayı2:"))
    if(ebob1(sayi1)and ebob2(sayi2)):
        if(liste1[-1]==liste2[-1]):
            print(liste1[-1],"ebob")                
        else:
            print("ebob yok")

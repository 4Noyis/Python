
liste=list()
def islem(sayi):
    if(sayi==0):
        return False
    else:    
        for i in range(1,sayi+1):
            if(sayi%i==0):
                liste.append(i)             
        return True    
                    
while True:
    sayi=int(input("Sayı:"))

    if(islem(sayi)):
        print(liste)
        liste.clear()
    else:
        break   
    
       
        
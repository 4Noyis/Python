print("""*********************
Hesap Makinesi

1 = Matematik işlemi
2 = Çıkartma İşlemi
3 = Çarpma İşlemi 
4 = Bölme İşlemi

*********************
""")

işlem=int(input("İşlemi seçiniz:"))

a=int(input("Sayı 1'i giriniz: "))
b=int(input("Sayı 2'yi giriniz: "))

if(işlem==1):
    print("{} ve {} toplamı {}'dır. ".format(a,b,a+b))
elif(işlem==2):
    print("{} ve {} farkı {}'dır. ".format(a,b,a-b))    
elif(işlem==3):
    print("{} ve {} çarpımı {}'dır. ".format(a,b,a*b))  
elif(işlem==4):
    print("{} ve {} bölümü {}'dır. ".format(a,b,a/b))      
else:
    print("HATALI İŞLEM...")    

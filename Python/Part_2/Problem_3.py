#Problem 3
#Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

#    Vize1 toplam notun %30'una etki edecek.

#    Vize2 toplam notun %30'una etki edecek.

#    Final toplam notun %40'ına etki edecek.


#    Toplam Not >=  90 -----> AA

#    Toplam Not >=  85 -----> BA

#    Toplam Not >=  80 -----> BB

#    Toplam Not >=  75 -----> CB

#    Toplam Not >=  70 -----> CC

#    Toplam Not >=  65 -----> DC

#    Toplam Not >=  60 -----> DD

#    Toplam Not >=  55 -----> FD

#    Toplam Not <  55 -----> FF

s1=int(input("1.Vize Notunuzu Giriniz: "))
s2=int(input("2.Vize Notunuzu Giriniz: "))
s3=int(input("Final Notunuzu Giriniz: "))

s4=(s1*0.3)+(s2*0.3)+(s3*0.4)

print("Vize 1:{}\nVize 2:{}\nFinal:{}\nSonuç:{} ".format(s1,s2,s3,s4))

if(s4>=90 ):
    print("AA")
elif(s4>=  85):
    print("BA")    
elif(s4>=  80):
    print("BA")    
elif(s4>=  75):
    print("BB")    
elif(s4>=  70):
    print("CB")    
elif(s4>=  65):
    print("CC")            
elif(s4>=  60):
    print("DC")  
elif(s4>=  55):
    print("DD")  
elif(s4>=  50):
    print("FD")  
elif(s4<  55):
    print("FF")  
else:
    print("HATALI VERİ GİRDİNİZ...")                
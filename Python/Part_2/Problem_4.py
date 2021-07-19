#Problem 4
#Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
#Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
  #dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
#Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , 
  #eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor"


soru=input("İstediğiniz Şekli Belirtin: ")

if(soru=="Dikdörtgen"or soru=="dikdörtgen"):
    k1=int(input("1.Kenarı girin: "))
    k2=int(input("2.Kenarı girin: "))
    k3=int(input("3.Kenarı girin: "))
    k4=int(input("4.Kenarı girin: "))
    if(k1==k2==k3==k4):
        print("Bu bir kare.")
    elif(k1==k2 or k1==k3 or k1==k4 or k2==k3 or k2==k3 or k2==k4 or k3==k4):
        print("Bu bir ikizkenar Dörtgen.")    
    elif(k1 != k2 != k3 != k4):
        print("Bu bir çeşitkenar Dörtgen.")

elif(soru=="Üçgen" or soru=="üçgen"):
    a=int(input("1.Kenarı girin: "))
    b=int(input("2.Kenarı girin: "))
    c=int(input("3.Kenarı girin: "))
    if(abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b):
        print("Yaptığınız üçgen üçgen kuralına uyuyor.")
        if(a==b or a==c or b==c ):
            print("Bu bir ikizkenar üçgen.")
        elif(a!=b and a!=c and c!=b):
            print("Bu bir çeşitkenar üçgen.")
        elif(a==b==c):
            print("Bu bir eşkenar üçgen.")
    else:
        print("Yazdığınız üçgen kuralına uymayan bir üçgen.")                 

elif(soru!="Dikdörtgen" or soru!="dikdörtgen" or soru!="Üçgen" or soru!="üçgen"):
    print("bum")
#Problem 2
#Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

s1=int(input("1.Sayı: "))
s2=int(input("2.Sayı: "))
s3=int(input("3.Sayı: "))

if(s1>s2 and s1>s3):
    print("Sayu 1 En Büyük.")
elif(s2>s3 and s2>s1):
    print("Sayı 2 En Büyük.")
elif(s3>s2 and s3>s1):
    print("Sayu 3 En büyük.")        
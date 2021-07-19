#Problem 1
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

s1=int(input("1.Sayı:"))
s2=int(input("2.Sayı:"))
s3=int(input("3.sayı:"))


print("{} , {} ve {} 'ın çarpımı {} dir ".format(s1,s2,s3,s1*s2*s3))
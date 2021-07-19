#Problem 3
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın 
#    ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

#veriler
yakıt=float(input("Aracınızzın kilometre başına yaktığı yakıt miktarını yazınız: "))
km=float(input("Kaç kilometre olduğunu yazın: "))

print("{} kilometre yolda ödemeni gereken tutar {}tl. ".format(km,km*yakıt))
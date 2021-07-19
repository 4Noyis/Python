#Problem 2
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

#Boy ve kilo değeri
boy=float(input("Boyunuzu giriniz:"))
kilo=float(input("Kilonuzu giriniz:"))

print("Kilonuz: {}\nBoyunuz: {}\nKitle Endeksiniz: {}\n".format(kilo,boy,kilo/boy))
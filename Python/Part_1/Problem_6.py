#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2

a=float(input("Üçgenin ilk dik kenraının uznuluğunu girin:"))
b=float(input("Üçgenin ikinci dik kenarının uzunluğunu girin:"))

#c=Hipotenüs

c=(a**2+b**2)**0.5

print("Hipotenüs uzunluğu:",c)







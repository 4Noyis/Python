# ax^2 + bx +c
# Delta = b**2-4*a*c
# Kök1=(-b + delta**0.5) / (2 * a)
# Kök2=(-b - delta**0.5) / (2 * a)

# Değer Alma
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

# Delta Hesaplama
Delta= b**2 - 4*a*c
print("Delta:1",Delta)

# Kökleri Bulma
x1=(-b + Delta**0.5) / (2*a)
x2=(-b - Delta**0.5) / (2*a)

# Kökleri yazdırma Sonuç
print("birinci Kök: {}\nİkinci Kök: {}\n ".format(x1,x2))

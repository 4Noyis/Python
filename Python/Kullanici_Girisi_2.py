print("""
***********************
Kullanıcı Giriş Paneli
***********************
""")

sys_kullanici= "noyis"
sys_sifre="123"
Giris_Hakki=3

while True:
    Id=input("Kullanıcı Adını Girin: ")
    sifre=input("Sifrenizi girin: ")
    
    if(Id != sys_kullanici and sifre==sys_sifre):
        print("Kullanıcı Adı Hatalı..")
        Giris_Hakki -=1
    elif(Id==sys_kullanici and sifre !=sys_sifre):
        print("Şifre Hatalı...")
        Giris_Hakki-=1
    elif(Id != sys_kullanici and Id !=sys_sifre):
        print("Kullanıcı Adı ve Şifre Hatalı...")
        Giris_Hakki -=1
    else:
        print("Giris Yapıldı") 
        break       
    
    if(Giris_Hakki==0):
        print("Giriş Hakkınız Kalmamıştır..")
        break    
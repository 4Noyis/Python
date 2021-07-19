# Proje 2
# Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

# Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.


class bilgisayar():
    
    def __init__(self,anakart="Boş",işlemci="Boş",ram="Boş",ekrankartı="Boş",depolama="Boş"):
        self.anakart=anakart
        self.işlemci=işlemci
        self.ram=ram
        self.ekrankartı=ekrankartı
        self.depolama=depolama
    
    def motherboard(self,anakart_ismi):
        self.anakart=anakart_ismi

    def CPU(self,işlemci_ismi):
        self.işlemci=işlemci_ismi  

    def RAM(self,ram_ismi):
        self.ram=ram_ismi

    def GPU(self,ekrankartı_ismi):
        self.ekrankartı=ekrankartı_ismi

    def Memory(self,depolama_ismi):
        self.depolama=depolama_ismi

    def __str__(self):
        return " Anakart:{}\n İşlemci:{}\n Ram:{}\n Ekran Kartı:{}\n Depolama:{}\n ".format(self.anakart,self.işlemci,self.ram,self.ekrankartı,self.depolama)

PC=bilgisayar()

while True:
    işlem=input("işlem:")
    
    if(işlem=="1"):
        anakart_ismi=input("Anakart: ")
        PC.motherboard(anakart_ismi)
        işlemci_ismi=input("İşlemci: ")
        PC.CPU(işlemci_ismi)
        ram_ismi=input("Ram:")
        PC.RAM(ram_ismi)
        ekrankartı_ismi=input("Ekran Kartı: ")
        PC.GPU(ekrankartı_ismi)
        depolama_ismi=input("Depolama İsmi: ")
        PC.Memory(depolama_ismi)
        print(PC)
    
    elif(işlem=="2"):
        pass
        
    else:
        break
        
        

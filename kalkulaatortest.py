class cal():                            # klassi nimi on cal
    def __init__(self,a,b):             # see võtab kaks arvu mida kasutada
        self.a = a
        self.b = b

    def liitmine(self):                 # liidab kaks arvu
        return self.a + self.b
    def lahutamine(self):               # lahutab teise arvu esimesest
        return self.a - self.b
    def korrutamine(self):              # korrutab kaks arvu
        return self.a * self.b
    def jagamine(self):                 # jagab esimese arvu teisega
        return self.a / self.b
    def jaak(self):                     # leiab jäägi jagamisest
        return self.a % self.b
    def ruutjuur(self):                 # leiab esimese arvu ruutjuure
        return self.a ** 0.5  # enne oli self.a ** self.b, see tegi valesti
    
    # uued funktsioonid
    def keskmine(self):                 # leiab kahe arvu keskmise
        return (self.a + self.b) / 2
    
    def absoluut(self):                 # leiab esimese arvu absoluutväärtuse
        return abs(self.a)
    
    def suurem(self):                   # kontrollib kas esimene arv on suurem
        if self.a > self.b:
            return True
        else:
            return False

# küsime kasutajalt numbreid
a = int(input("Sisesta esimene number: "))          
b = int(input("Sisesta teine number: "))

kalk = cal(a,b)                         

while True:
    def menu():                         # menüü mida kasutaja näeb
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine') 
        x = x + '\n7. Keskmine\n8. Absoluut\n9. Suurem'  # uued valikud
        print(x)
    
    menu()                               # näitab menüüd
    valik = int(input('Sisesta üks valikutest: '))  # kasutaja valib
    
    # vaatame mis kasutaja valis
    if valik == 1:                       # liitmine
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:                     # lahutamine
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:                     # korrutamine
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:                     # jagamine
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:                     # jäägi leidmine
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:                     # ruutjuure leidmine
        print("Vastus: ",kalk.ruutjuur())
        break
    elif valik == 7:                     # keskmise leidmine
        print("Vastus: ",kalk.keskmine())
        break
    elif valik == 8:                     # absoluutväärtuse leidmine
        print("Vastus: ",kalk.absoluut())
        break
    elif valik == 9:                     # suurema arvu kontroll
        print("Vastus: ",kalk.suurem())
        break
    elif valik == 0:                     # lõpetamine
        print('Sisesta uuesti üks liitmise operaator')
        break
       #https://urban-sniffle-r45jrw9x4x7g3p7qr.github.dev/
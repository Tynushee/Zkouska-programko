#Motivace - Vybrala jsem si RPG hru, kde můj cíl byl vytvořit vesnici, kde si hráč může zajít na pivo, čímž si obnoví zdraví, nebo také vylepšovat vylepšovat 
#Zbraně a vrátit se zpátky na bojiště, kde má 3 nestvůry, poslední je boss. 



import random

class Postava:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.hp = 100
        self.xp = 0
        self.uroven = 1
        self.uroven_zbrane = 1
    
    def dej_si_pivo(self):
        print(f"{self.jmeno} si dává pivo a odpočívá.")
        self.hp = 100  # Obnoví zdraví
    
    def vylepsi_zbran(self):
        if self.xp >= 10 * self.uroven_zbrane:
            self.xp -= 10 * self.uroven_zbrane
            self.uroven_zbrane += 1
            print(f"Zbraň vylepšena na úroveň {self.uroven_zbrane}!")
        else:
            print("Nemáš dost XP na vylepšení zbraně.")
    
    def zobraz_statistiky(self):
        print(f"Jméno: {self.jmeno}")
        print(f"HP: {self.hp}")
        print(f"XP: {self.xp}")
        print(f"Úroveň zbraně: {self.uroven_zbrane}")

class Nestvura:
    def __init__(self, jmeno, hp, odmena_xp):
        self.jmeno = jmeno
        self.hp = hp
        self.odmena_xp = odmena_xp
    
    def utok(self, postava):
        poskozeni = random.randint(5, 15)
        postava.hp -= poskozeni
        print(f"{self.jmeno} útočí a způsobuje {poskozeni} poškození.")
    
    def utrpi_poskozeni(self, poskozeni):
        self.hp -= poskozeni
        print(f"{self.jmeno} dostává {poskozeni} poškození.")

def vytvor_postavu():
    jmeno = input("Zadejte jméno postavy: ")
    return Postava(jmeno)

def bitva(postava, nestvura):
    print(f"Bojuješ s {nestvura.jmeno}!")
    while postava.hp > 0 and nestvura.hp > 0:
        akce = input("Zvol akci (útok/útěk): ").lower()
        if akce == "útok":
            poskozeni = random.randint(5, 15) * postava.uroven_zbrane
            nestvura.utrpi_poskozeni(poskozeni)
            if nestvura.hp > 0:
                nestvura.utok(postava)
        elif akce == "útěk":
            print("Úspěšně jsi utekl!")
            return
        else:
            print("Neplatná akce.")
    
    if postava.hp > 0:
        print(f"Porazil jsi {nestvura.jmeno} a získal {nestvura.odmena_xp} XP!")
        postava.xp += nestvura.odmena_xp
        print("Vracíš se zpět do vesnice.")
    else:
        print(f"Byl jsi poražen {nestvura.jmeno}.")
        print("Musíš se vrátit do vesnice a vyléčit se.")

def vesnice(postava):
    while True:
        akce = input("Vesnice (pivo/vylepšit/bojiště/odchod): ").lower()
        if akce == "pivo":
            postava.dej_si_pivo()
        elif akce == "vylepšit":
            postava.vylepsi_zbran()
        elif akce == "bojiště":
            bojiste(postava)
            break
        elif akce == "odchod":
            break
        else:
            print("Neplatná akce.")
    
def bojiste(postava):
    while True:
        print("Dostupné nestvůry:")
        print("1. Zombík (HP: 30, XP: 10)")
        print("2. Goblin (HP: 50, XP: 20)")
        print("3. Wisman (HP: 100, XP: 50)")
        
        volba = input("Zvol proti komu chceš bojovat (1/2/3) nebo 'zpět' pro návrat do vesnice: ").lower()
        if volba == '1':
            bitva(postava, Nestvura("Zombík", 30, 10))
            if postava.hp <= 0:
                print("Musíš se vrátit do vesnice a vyléčit se.")
                vesnice(postava)
                break
        elif volba == '2':
            bitva(postava, Nestvura("Goblin", 50, 20))
            if postava.hp <= 0:
                print("Musíš se vrátit do vesnice a vyléčit se.")
                vesnice(postava)
                break
        elif volba == '3':
            bitva(postava, Nestvura("Wisman", 100, 50))
            if postava.hp <= 0:
                print("Musíš se vrátit do vesnice a vyléčit se.")
                vesnice(postava)
                break
        elif volba == 'zpět':
            vesnice(postava)
            break
        else:
            print("Neplatná volba.")
            continue

def hlavni():
    postava = vytvor_postavu()
    while True:
        postava.zobraz_statistiky()
        volba = input("Kam chceš jít? (vesnice/bojiště/konec): ").lower()
        if volba == "vesnice":
            vesnice(postava)
        elif volba == "bojiště":
            bojiste(postava)
        elif volba == "konec":
            print("Hra skončila.")
            break
        else:
            print("Neplatná akce.")

if __name__ == "__main__":
    hlavni()


#Zdroje - https://chatgpt.com/?oai-dm=1, https://www.python.org/, kamarád(pomohl mi opravit v kódu chybu, na které nedošlo ani ChatGPT), https://www.youtube.com/watch?v=xHPmXArK6Tg&list=PL1-slM0ZOosXf2oQYZpTRAoeuo0TPiGpm&index=2 (zde byl použitý class, kde jsem se inspirovala)
#Nejdříve jsme definovali třídy, tímpádem jsem vybrala Class(použitý k definici nových tříd) Nestvura a Postava, kde jsem určila jméno XP atd.. Poté máme bojování na bojišti, kde má hráč možnost bojovat proti 3 nestvůrám. Dále jsem taky umožnila návrat do vesnice kde si hráč dokáže dát pivo. Strávila jsem u toho asi 5 hodin dohromady.
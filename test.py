from pom import reci
import random

def izbor_reci():
    rec = reci[random.randint(0, len(reci))].upper()
    return rec

zadata_rec = izbor_reci()
upotrebljena_slova = set()
zivota = 7

# print(zadata_rec)
# print(len(zadata_rec))

prikaz_rezultata = "_ "*len(zadata_rec)
print(prikaz_rezultata)

zavrseno = False
while zivota > 0 and zavrseno == False:
    pogodak = False
    pokusaj = input("Unesite slovo koje mislite da ima u zadatoj reci: ").upper()
    if pokusaj.isalpha() and len(pokusaj) == 1: # Ako je uneto slovo i ako je unet string duzine 1 radi se ...
        if pokusaj not in upotrebljena_slova:
            upotrebljena_slova.add(pokusaj) # Dodaje se upotrebljeno slovo u set
            for i in range(len(zadata_rec)):
                if zadata_rec[i] == pokusaj:
                    pogodak = True
                    prikaz_rezultata = prikaz_rezultata[:i*2]+pokusaj+prikaz_rezultata[i*2+1:]
            print("***************")
            print(prikaz_rezultata)
            if not pogodak:
                zivota -=1
            print("Preostalo netacnih pokusaja:", zivota)
            if "_" not in prikaz_rezultata:
                zavrseno = True
        else:
            print("Vec ste probali slovo ", pokusaj) # Ako je slovo vec pokusano
    else:
        print("Nepravilan unos!!!!") # Ako unos nije slovo vec broj ili vise slova i brojeva

if zavrseno:
    print("Bravo pogodili ste trazeni pojam!!!")
else:
    print("Ponestalo vam je pokusaja! KRAJ")
    print("Trebalo je da pogodite sledeci pojam:", zadata_rec)

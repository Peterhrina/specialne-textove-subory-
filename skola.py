#odrbavacia hra s benfordovym zakonom-vygeneruje 2 nahodne cisla od 100 do 1000. jedno cislo umocnim na druhe
#zistit prvu cifru tohto cisla a nasledne pocitat jej vyskyt a vypisat absolutnu aj relativnu
import random
pocetnost = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
pocet_opakovani = 10000
for i in range(pocet_opakovani):
    x = random.randrange(100, 1001)
    y = random.randrange(100, 1001)
    vysledok = x**y
    cifra = int(str(vysledok)[0])
    pocetnost[cifra] += 1
for i in pocetnost:
    print(round((pocetnost[i]/pocet_opakovani)*100, 2), end = ',')

print(pocetnost)
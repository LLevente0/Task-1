"""2. feladat: Oszthatóság	14 pont
Írjon programot oszthato.py néven. A programban hozzon létre egy függvényt oszthato néven,
ami egy egész számot kap paraméterként és igaz értéket ad vissza, ha a szám 7-tel osztható, de 3-mal nem.
A függvény segítségével számolja ki azon 3 jegyű számok átlagát, amire a függvény igaz értékkel tér vissza.
Minta:
A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga: 551.2705882352941"""

haromjegyu_szamok = []

for szam in range(100, 1000):
    if szam % 7 == 0 and szam % 3 != 0:
        haromjegyu_szamok.append(szam)

# print(haromjegyu_szamok)

def oszthato(szamok):
    osszeg = sum(szamok)
    darab_szamok = len(szamok)
    atlag = osszeg / darab_szamok
    return atlag

print(oszthato(haromjegyu_szamok))
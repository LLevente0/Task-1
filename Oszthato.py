"""2. feladat: Oszthatóság	14 pont
Írjon programot oszthato.py néven. A programban hozzon létre egy függvényt oszthato néven,
ami egy egész számot kap paraméterként és igaz értéket ad vissza, ha a szám 7-tel osztható, de 3-mal nem.
A függvény segítségével számolja ki azon 3 jegyű számok átlagát, amire a függvény igaz értékkel tér vissza.
Minta:
A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga: 551.2705882352941"""


haromjegyu = []

def oszthatosag(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        haromjegyu.append(szam)
        return True
    else:
        return False

print(oszthatosag(7))

def atlag(szamok):
    # osszeg = 0
    # for szam in szamok:
    #     osszeg += szam
    #    osszeg = osszeg + szam
    osszeg = sum(szamok)
    print(osszeg)
    hany_darab_szam = len(szamok)
    print(hany_darab_szam)

atlag(haromjegyu)
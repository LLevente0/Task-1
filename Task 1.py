ar = int(input("Kérem a termék árát forintban: "))
arfolyam = int(input("Kérem az euro árfolyamát: "))
euro = int(input("Mennyi euróval rendelkezel: "))


if ar / arfolyam > euro:
    print("Nincs elég euród a termék megvásárlására!")
else:
    print("A terméket meg tudod vásárolni!")

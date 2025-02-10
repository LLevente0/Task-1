ar = float(input("Kérem a termék árát forintban: "))
arfolyam = float(input("Kérem az euro árfolyamát: "))
euro = float(input("Mennyi euróval rendelkezel: "))


if ar / arfolyam > euro:
    print("Nincs elég euród a termék megvásárlására!")
else:
    print("A terméket meg tudod vásárolni!")

kapacita = int(open("bus_vytazenost.txt", "r").readline()[0:2])
bus = [riadok.strip() for riadok in open("bus_vytazenost.txt", "r", encoding="utf-8").readlines()][1:]

zastavky = {}
z = ""
pocet = 0
for zastavka in bus:
    udaje = zastavka.split()
    pocet += int(udaje[0]) - int(udaje[1])
    b = " ".join([udaje[i] for i in range(len(udaje)) if i > 1])
    z += "{}, ".format(b)
    zastavky[b] = zastavky.get(b, pocet)
print("Počet zastávok: {} \nZastávky: {}".format(len(zastavky), z))

prekrocili = []
for zastavka, pocet in zastavky.items():
    if pocet > kapacita:
        prekrocili.append(zastavka)
print("Zastávky, kde po nastúpení ľudí bol autobus preplnený: {}".format(", ".join(prekrocili)))

m = max(zastavky.values())
if m > kapacita:
    print("Najvyšší počet ľudí nad rámec kapacity bol: {}".format(m))

sutaziaci = [riadok.strip().split() for riadok in open("skok_do_dialky.txt", "r").readlines()]
krajiny = []
pocty = {}
skoky = {}
for sutaz in sutaziaci:
    pocty[sutaz[1]] = pocty.get(sutaz[1], 0) + 1
    skoky[sutaz[0]] = skoky.get(sutaz[0], max(sutaz[2:]))
    if sutaz[1] not in krajiny:
        krajiny.append(sutaz[1])
print("Zoznam krajín: {}".format(", ".join(krajiny)))

for krajina, pocet in pocty.items():
    print("Krajina: {} počet súťažiacich: {}".format(krajina, pocet))

m = max(skoky.values())
vitazi = []
for vitaz, maxi in skoky.items():
    if maxi == m:
        vitazi.append(vitaz)
print("Najďalej skočil/li: {}".format(", ".join(vitazi).strip(",")))

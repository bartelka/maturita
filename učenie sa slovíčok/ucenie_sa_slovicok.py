def skusaj():
    global znova, nespravne
    print("Opätovné skúšanie:")
    while len(znova) > 0:
        for i in znova:
            print(i)
            slovo = input()
            if slovo in d and i == z[d.index(slovo)]:
                znova.remove(i)
        nespravne += 1
    print("Počet nesprávnych odpovedí: {}".format(nespravne-1))

slovicka = [riadok.strip() for riadok in open("ucenie_sa_slovicok.txt", "r", encoding="utf-8").readlines()]
z = [slovicka[i] for i in range(len(slovicka)) if i % 2 == 0]
d = [slovicka[i] for i in range(len(slovicka)) if i % 2 == 1]

aas = input("zadavat anglicky - a / slovensky - s: ")
if aas == "a":
    z, d = d, z

znova = []
nespravne = 0
for i in z:
    print(i)
    slovo = input()
    if slovo in d and i != z[d.index(slovo)]:
        znova.append(i)
        nespravne += 1
    elif slovo not in d:
        znova.append(i)
        nespravne += 1

skusaj()

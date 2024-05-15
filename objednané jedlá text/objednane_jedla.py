fr = open("objednane_jedla.txt", "r")
jedielka = [jedlo.strip().split(" ") for jedlo in fr.readlines()]
jedla = {}
menej_20 = ""
viac_20 = ""
print("Počet objednaných jedál: {}".format(len(jedielka)))

for jedlo in jedielka:
    jedla[jedlo[1]] = jedla.get(jedlo[1], 0) + 1
for jedlo, pocet in jedla.items():
    print("{} stravníkov si objednalo jedlo: {}".format(pocet, jedlo))
    if pocet < 20:
        menej_20 += "{} ".format(jedlo)
    else:
        viac_20 += "{} ".format(jedlo)
print("Menej ako 20 stravníkov si objednali jedlo/jedlá: {}".format(menej_20.strip()))
print("Jedlá, ktoré si objednalo dostatok stravníov: {}".format(viac_20.strip()))

vyjadrenia = [riadok.strip().split(" ") for riadok in open("spokojnost_1.txt", "r",encoding="utf-8").readlines()]
print("Počet vyjadrení: {}".format(len(vyjadrenia)))

pvh = {}
hodiny = []
minuty = []
for den in vyjadrenia:
    hodina = int(den[0].split(":")[0])
    minuta = int(den[0].split(":")[1])
    pvh[hodina] = pvh.get(hodina, 0) + 1
    hodiny.append(hodina)
    minuty.append(minuta)

for hodina, pocet in pvh.items():
    print("Počas {}-tej hodiny bolo {} vajadrení".format(hodina, pocet))

pd = 0
pocet = 1
dni = {}
for i in range(len(hodiny)-1):
    if hodiny[i] == hodiny[i+1] and minuty[i] > minuty[i+1]:
        pd += 1
        dni[pd] = dni.get(pd, pocet)
        pocet = 1
    elif hodiny[i] > hodiny[i+1]:
        pd += 1
        dni[pd] = dni.get(pd, pocet)
        pocet = 1
    else:
        pocet += 1

for den, pocet in dni.items():
    print("Počas {}-ho dňa bolo vyjadrení {}".format(den, pocet))

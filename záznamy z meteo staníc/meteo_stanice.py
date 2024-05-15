fr = open("meteo_stanice.txt", "r", encoding="utf-8")

zaznamy = [riadok.strip(). split(" ") for riadok in fr.readlines()]
print("Počet meraní: {}".format(str(len(zaznamy))))
teploty = [zaznam[3].replace(",", ".") for zaznam in zaznamy]
tep = []
sucet = 0
for i in range(len(teploty)):
    teplota = float(teploty[i][1:])
    if teploty[i][0] == "-":
        teplota *= -1
    sucet += teplota
    tep.append(teplota)
    print("{}. teplota je {}°C".format(i+1, teplota))

max_teplota = max(tep)
max_stanica = zaznamy[tep.index(max_teplota)][0]

print("Najvyššie nameraná teplota je {}°C, ktorá bola nameraná na stanici {}.".format(max_teplota, max_stanica))
print("Priemerná teplota všetkých staníc je {}°C".format(round(sucet/len(tep), 2)))

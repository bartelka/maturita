zastavky = [riadok.strip().split(";") for riadok in open("dopravny_prieskum.txt", "r", encoding="utf-8")]

automat = []
znamenie = []
pocty = []
pocet = 0
for z in zastavky:
    nastup, vystup, zastavka = int(z[0]), int(z[1]), z[2]
    pocet += nastup - vystup
    pocty.append(pocet)
    if nastup >= 10:
        automat.append(zastavka)
    if nastup < 3 and vystup < 3:
        znamenie.append(zastavka)
    print("Zastávka: {} počet cestujúcich v električke po odchode: {}".format(zastavka, pocet))
if max(pocty) > 80:
    print("typ električky: dlhá")
elif 80 >= max(pocty) > 30:
    print("typ električky: štandartná")
else:
    print("typ električky: krátka")

print("Zoznam vhodných zastávok na umiestnenie automatu: {}".format(", ".join(automat).strip(", ")))
print("Zoznam zastávok na znamenie: {}".format(", ".join(znamenie).strip(", ")))

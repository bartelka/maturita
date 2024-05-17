import random

def generuj_prilad():
    return "{} * {}".format(random.randint(1,10), random.randint(1,10))

fw = open("nasobilka_vystup.txt", "w")
priklady = {}
for _ in range(10):
    priklad = generuj_prilad()
    priklady[priklad] = priklady.get(priklad, int(priklad.split("*")[0]) * int(priklad.split("*")[1]))
    fw.write("{} = {}\n".format(priklad, int(priklad.split("*")[0]) * int(priklad.split("*")[1])))

bodiky = 10
zp = []
for priklad, vysledok in priklady.items():
    v = input("Vyrieš príklad {}: ".format(priklad))
    if int(v) != vysledok:
        zp.append(priklad)

if len(zp) != 0:
    for priklad in zp:
        bodiky -= 1
        v = input("Znovu vyrieš príklad {}: ".format(priklad))

print("Počet bodíkov: {}".format(bodiky))

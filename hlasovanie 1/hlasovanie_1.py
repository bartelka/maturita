fr = open("hlasovanie_1.txt", "r")
hlasy = [hlas.strip() for hlas in fr.readlines()]
fr = open("hlasovanie_vypadnuti.txt", "r")
vypadnuti = [hlas.strip() for hlas in fr.readlines()]

hlasovanie = {}
print("Počet zaslaných SMS: {}". format(len(hlasy)))
for hlas in hlasy:
    hlasovanie[hlas] = hlasovanie.get(hlas, 0) + 1

najmenej = min(hlasovanie.values())
min_hlasy = ""
vyp_hlasy = ""
for hlas, pocet in hlasovanie.items():
    print("Súťažiaci s telefónnym číslom {} získal {} hlasov".format(hlas, pocet))
    if pocet == najmenej:
        min_hlasy += "{}, ".format(hlas)
    if pocet == najmenej and hlas not in vypadnuti:
        vyp_hlasy += "{}, ".format(hlas)
print("Súťažiaci, ktorí dostali najmenej bodov a nepostupujú sú {}.".format(min_hlasy.strip(", ")))
print("Súťažiaci, ktorí dostali najmenej bodov, nie sú medzi vypadnutými a nepostupujú sú {}.".format(vyp_hlasy.strip(", ")))

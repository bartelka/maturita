vyjadrenia = [riadok.strip().split(" ") for riadok in open("spokojnost_1.txt", "r",encoding="utf-8").readlines()]
print("Počet vyjadrení: {}".format(len(vyjadrenia)))

spokoj = {}
nespokoj = {}
for i in vyjadrenia:
    hod = i[0].split(":")[0]
    if i[1] == "áno":
        spokoj[hod] = spokoj.get(hod, 0) + 1
    elif i[1] == "nie":
        nespokoj[hod] = nespokoj.get(hod, 0) + 1

print("Počas {}-tej hodiny bolo spokojných najviac zákazníkov s počtom: {}".format(*[hod for hod, pocet in spokoj.items()
                                                                                     if pocet == max(spokoj.values())], max(spokoj.values())))
print("Počas {}-tej hodiny bolo nespokojných najviac zákazníkov s počtom: {}".format(*[hod for hod, pocet in nespokoj.items()
                                                                                     if pocet == max(nespokoj.values())], max(nespokoj.values())))
print(spokoj, nespokoj)

for hod, pocet in spokoj.items():
    if hod in nespokoj.keys():
        p = pocet + nespokoj[hod]
        percento = round(pocet / p * 100, 2)
        print("Počas {}-tej hodiny bolo spokojných {}% zákazníkov.".format(hod, percento))
    if hod not in nespokoj.keys():
        percento = round(100, 2)
        print("Počas {}-tej hodiny bolo spokojných {}% zákazníkov.".format(hod, percento))

vstup = input("vstup: ")
sifry = {"0": [" "], "1": ["A", "B", "C"], "2": ["D", "E", "F"], "3": ["G", "H", "I"], "4": ["J", "K", "L"],
         "5": ["M", "N", "O"], "6": ["P", "Q", "R"], "7": ["S", "T", "U"], "8": ["V", "W", "X"], "9": ["Y", "Z"]}
pocetnost = {}
for i in vstup:
    pocetnost[i] = pocetnost.get(i,0) + 1

vystup = []
tabulka = {}
for i in vstup:
    for sifra, znak in sifry.items():
        if i in znak:
            nasobok = znak.index(i) + 1
            vystup.append(sifra * nasobok)
            tabulka[sifra] = tabulka.get(sifra, 0) + nasobok
m = max(tabulka.values())
najviac = [znak for znak, pocet in tabulka.items() if pocet == m]

print(*vystup)
print("Najčastejšie zvolené políčka: {}".format(*najviac))

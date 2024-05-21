# zobrazí text z textového súboru na obrazovku,
# vypíše jednotlivé počty znakov anglickej abecedy v tvare znak – počet_výskytov; malé a veľké
# písmená nerozlišuje, ostatné znaky ignoruje,
# vypíše zoznam znakov, ktoré sa v texte vôbec nevyskytli.
from string import ascii_lowercase
suborik = [riadok.strip() for riadok in open("tabulka_pocetnosti.txt", "r", encoding="utf-8")]
abeceda = {}

for i in ascii_lowercase:
    abeceda[i] = abeceda.get(i, 0)

for riadok in suborik:
    print(riadok)
    for i in riadok:
        if i.lower() in ascii_lowercase:
            abeceda[i.lower()] += 1

nevyskytli = []
for znak, pocet in abeceda.items():
    if pocet > 0:
        print("znak: {} počet výskytov znaku: {}".format(znak, pocet))
    else:
        nevyskytli.append(znak)
print("Zoznam zankov, ktoré sa nevyskytli: {}".format(",".join(nevyskytli).strip(",")))

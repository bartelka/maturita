import random

def precitanie_suboru():
    return [riadok.strip() for riadok in open("poprehadzovany_text1_vstup.txt", "r", encoding="utf-8").readlines()]
def vypisanie_textu(zoznam):
    for i in zoznam:
        print(i)
def poprehadzovanie(text):
    vystup = []
    fw = open("poprehadzovany_text1.txt", "w", encoding="utf-8")
    for riadok in text:
        riadok = riadok.strip().split()
        row = ""
        for i in range(len(riadok)):
            if len(riadok[i]) == 1 :
                row += riadok[i]
            else:
                s = list(riadok[i])[1:-1]
                random.shuffle(s)
                slovo = "{}{}{} ".format(riadok[i][0], "".join(s), riadok[i][-1])
                row += slovo
        vystup.append(row)
        fw.write("{}\n".format(row))
    return vystup

text = precitanie_suboru()
vypisanie_textu(text)
print(100*"*")
vypisanie_textu(poprehadzovanie(text))

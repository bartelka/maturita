# Prečíta a vypíše zo súboru šírku a výšku obrázka a počet všetkých bodov.
# Prečíta prvý riadok obrázka a pošle ho na spracovanie funkcii spracuj_riadok().
# Obsahuje funkciu spracuj_riadok(), ktorá z postupnosti núl a jednotiek vyrobí výstupný textový
# reťazec. Vo výstupe budú za sebou idúce nuly nahradené ich počtom a rovnako za sebou idúce
# jednotky budú nahradené ich počtom. Na začiatku výstupného reťazca bude počet núl na začiatku
# vstupného reťazca. V prípade, že vstupný reťazec začína jednotkami, na začiatku výstupného reťazca
# bude 0, vyjadrujúca nula núl na začiatku vstupu.
# Prečíta všetky riadky súboru, transformuje ich pomocou funkcie spracuj_riadok() a vytvorí nový
# textový súbor s názvom kompresia_obrazka_vystup.txt. Aj vo výstupnom súbore bude v
# prvom riadku uložená veľkosť obrázka.
def spracuj_riadok(riadok):
    pp = riadok[0]
    vystup = ""
    pocet = 0
    if pp != "0":
        vystup += "{} ".format("0")
    for i in riadok:
        if i != pp:
            vystup += "{} ".format(pocet)
            pocet = 1
            pp = i
        else:
            pocet += 1
    vystup += "{} ".format(pocet)
    return vystup

sv = open("kompresia_obrazka_1.txt", "r").readline().strip().split()
print("šírka: {} výška: {} počet bodov: {}".format(int(sv[0]), int(sv[1]), int(sv[0])*int(sv[1])))
fr = [riadok.strip() for riadok in open("kompresia_obrazka_1.txt", "r").readlines()[1:]]
fw = open("kompresia_obrazka_vystup.txt", "w", encoding="utf-8")
fw.write("šírka: {} výška: {}\n".format(int(sv[0]), int(sv[1])))
for riadok in fr:
    fw.write("{}\n".format(spracuj_riadok(riadok)))
    print("{}".format(spracuj_riadok(riadok)))

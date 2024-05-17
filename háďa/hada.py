fr = [riadok.strip() for riadok in open("hada.txt", "r").readlines()]
print("Počet hier: {}".format(len(fr)))

dlzky = [len(hra) for hra in fr]
print("Najdlhšia hra mala {} krokov".format(max(dlzky)))

fw = open("hada_kopia.txt", "w")
for hra in fr:
    znak = hra[0]
    pocet = 0
    riadok = ""
    sucet = 0
    for krok in hra:
        sucet += 1
        if krok == znak:
            pocet += 1
        else:
            riadok += "{} {} ".format(znak, pocet)
            pocet = 1
            znak = krok
        if sucet == len(hra):
            riadok += "{} {} ".format(znak, pocet)
    fw.write("{}\n".format(riadok))

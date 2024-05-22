def spracuj_riadok():
    fw = open("konverzia_suboru_1_vystup.txt", "w")
    fw.write("{} {}\n".format(sv[0], sv[1]))
    for riadok in riadky:
        farbicky = [riadok[i:i+2] for i in range(0, len(riadok), 2)]
        f = []
        for farba in farbicky:
            x = int(farba, 16)
            if x < 128:
                x = 0
            else:
                x = 1
            f.append(str(x))
        fw.write("{}\n".format(" ".join(f)))

sv = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8").readline().strip().split()
print("šírka: {} výška: {} počet pixelov: {}".format(int(sv[0]), int(sv[1]), int(sv[0])*int(sv[1])))

riadky = [riadok.strip() for riadok in open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8").readlines()[1:]]
spracuj_riadok()

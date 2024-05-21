sutaziaci = [riadok.strip().split()[0] for riadok in open("sutaz_vbehu.txt", "r", encoding="utf-8")]
casy = [int(riadok.strip().split()[1]) for riadok in open("sutaz_vbehu.txt", "r", encoding="utf-8")]
print("Počet zúčastnených športovcov: {}".format(len(sutaziaci)))

m = min(casy)
naj = ""
for i in range(len(sutaziaci)):
    print("Súťažiaci {} dobehol do cieľa za {} sekúnd".format(sutaziaci[i], casy[i]))
    if casy[i] == m:
        naj = "Najlepší súťažiaci: {} čas: {}".format(sutaziaci[i], "{} min. {} sek.".format(m//60, m%60))
print(naj)

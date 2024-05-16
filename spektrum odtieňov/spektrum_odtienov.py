fr = open("ciernobiely_obrazok_1.txt", "r")
rozmery = fr.readline().strip().split()
w, h = int(rozmery[0]), int(rozmery[1])
print("šírka obrázka: {}\nvýška obrázka: {}\npočet bodov: {}".format(w, h, w*h))

pixely = [riadok.strip() for riadok in fr.readlines()]
farby = []
for riadok in pixely:
    farby.append([riadok[i:i+2] for i in range(0, len(riadok), 2)])

odtiene = {}
for y in farby:
    for x in y:
        odtiene[int(x, 16)] = odtiene.get(int(x,16), 0) + 1

odtiene = dict(sorted(odtiene.items()))

import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(width=len(odtiene)*2, height=500, background="white")
canvas.pack()

print("Počet výskytov najčastejštejšie vyskytovaného odtieňa je {}".format(max(odtiene.values())))
for farba, pocet in odtiene.items():
    canvas.create_rectangle(farba*2, 500 - pocet, farba*2 + 2, 500 , fill="gray", outline="gray")

win.mainloop()

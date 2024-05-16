def preklop():
    canvas.scale("all", (w*strana)/2, (h*strana)/2, -1, 1)

fr = open("preklopenie_obrazka.txt", "r")
rozmery = fr.readline().strip().split()
w, h = int(rozmery[0]), int(rozmery[1])
strana = 5
jednotky = 0
pocet_pixelov = w * h
pixely = [riadok.strip().split() for riadok in fr.readlines()]

import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(width=w*strana, height=h*strana, background="white")
canvas.pack()

for y in range(h):
    for x in range(w):
        if pixely[y][x] == "1":
            jednotky += 1
            canvas.create_rectangle(x * strana, y * strana, x * strana + strana, y * strana + strana, fill="black", outline="black")

print("Počet pixelov: {}, počet 1: {}".format(pocet_pixelov, jednotky))
button = tk.Button(win, text="Preklop", command=preklop)
button.pack()

win.mainloop()

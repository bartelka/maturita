suborik = [riadok.strip().split() for riadok in open("zastavba_na_ulici.txt", "r").readlines()]

def budovecka(x, vyska, sirka):
    if vyska == 0:
        canvas.create_line(x, h - 50, x + sirka, h - 50, fill="green", width=3)
    else:
        canvas.create_rectangle(x, h - vyska - 50, x + sirka, h - 50, fill="gray")

def ciara(x, v1, v2):
    canvas.create_line(x, h - 50 - v1, x, h - 50 - v2, fill="red", width=3, tags="line")

def vykresli():
    canvas.delete("line")
    rozdiel = int(v.get().strip())
    vysky = [int(r[0]) for r in suborik]
    x = 0
    for i in range(len(vysky) - 1):
        x += int(suborik[i][1])
        if abs(vysky[i] - vysky[i + 1]) > rozdiel:
            ciara(x, vysky[i], vysky[i + 1])

import tkinter as tk

w = 800
h = 300

win = tk.Tk()

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()

x = 0
for budova in suborik:
    budovecka(x, int(budova[0]), int(budova[1]))
    x += int(budova[1])

v = tk.Entry(win)
v.pack()

button = tk.Button(win, text="Vykresli", command=vykresli)
button.pack()

win.mainloop()

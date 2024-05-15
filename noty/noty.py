def osnova(y):
    for _ in range(5):
        canvas.create_line(0, y, w, y, fill="black")
        y += rozdiel

def kresli_noty():
    y = 20
    sx = 20
    x = w - 20
    vzdialenost = 20
    osnova(y)
    for i in noty:
        if sx > x:
            y += rozdiel * 8
            osnova(y)
            sx = 20
        nota = n[i]
        canvas.create_oval(sx, y + rozdiel * nota, sx + vzdialenost, y + rozdiel * (nota + 1))
        sx += vzdialenost

noty = [i for i in open("noty.txt", "r").readline().strip()]
n = {"c": 4.5, "d": 4, "e": 3.5, "f": 3, "g": 2.5, "a": 2, "h": 1.5}

import tkinter as tk
win = tk.Tk()

w = 300
h = 400
rozdiel = 10

canvas = tk.Canvas(width=w, height=h, background="white")
canvas.pack()

kresli_noty()

win.mainloop()

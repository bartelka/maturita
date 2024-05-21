def priebeh_hry(e):
    global pocet, hrac
    if e.char in "123":
        ciselko = int(e.char)
        if pocet - ciselko >= 0:
            pocet -= ciselko
            if pocet == 0:
                canvas.delete("all")
                canvas.create_text(w / 2, h / 2, text="Vyhral hráč číslo: {}".format(hraci[hrac]), font="Times 50")
            else:
                canvas.itemconfig(z, text="Počet zápaliek: {}".format(pocet))
                hrac = (hrac + 1) % 3
                canvas.itemconfig(t, text="Ťahá hráč: {}".format(hraci[hrac]))
                vykresli_hru(pocet, x, y)
        elif pocet - ciselko < 0:
            hrac = (hrac + 1) % 3
            canvas.itemconfig(t, text="Ťahá hráč: {}".format(hraci[hrac]))

def vykresli_hru(pocet, x , y):
    canvas.delete("zapalka")
    for i in range(pocet):
        zapalka(x, y)
        x += 20

def zapalka(x, y):
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow', tags="zapalka")
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown', tags="zapalka")

import tkinter as tk, random

pocet, hraci, hrac = 15, [1, 2, 3], 0
x, y = 50, 75
w, h = 650, 200
win = tk.Tk()

canvas = tk.Canvas(width=w, height=h)
canvas.pack()

t = canvas.create_text(w/2, 25, text="Ťahá hráč: {}".format(hraci[hrac]), font="times 12")
z = canvas.create_text(w/2, 45, text="Počet zápaliek: {}".format(pocet), font="times 12")
vykresli_hru(pocet, x, y)

canvas.bind_all('<Key>', priebeh_hry)

win.mainloop()

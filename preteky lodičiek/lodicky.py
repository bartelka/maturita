def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def plocha(x):
    global lx
    y = 30
    for i in range(15):
        lodicka(lx[i] + x[i], y)
        y += h / 15
        lx[i] += x[i]
    canvas.create_line(ciara, 0, ciara, h, fill="red")

def hra():
    global status
    if status:
        canvas.delete("all")
        px = [random.randint(1,10) for _ in range(15)]
        plocha(px)
        for i in range(15):
            if lx[i] >= ciara:
                status = False
                canvas.create_text(w/2, h/2, text="Vahrala lodička číslo: {}".format(i+1), font="Arial 20", fill="red")
        canvas.after(50, hra)

def mover(e):
    global status
    if status:
        hra()

import tkinter as tk, random

win = tk.Tk()

w, h= 700, 800
ciara = w - 20
pociatok = 20
lx = [pociatok] * 15
status = True

canvas = tk.Canvas(width=w, height=h)
canvas.pack()

plocha([0] * 15)

canvas.bind("<Button-1>", mover)

win.mainloop()

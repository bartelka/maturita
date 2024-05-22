from string import ascii_uppercase
def kresli_taniere():
    x = w / 10 - 50
    for i in range(10):
        canvas.create_oval(x-a1, h/2-a1, x+a1, h/2+a1, fill="blue", tags=ascii_uppercase[i])
        canvas.create_oval(x-a2, h/2-a2, x+a2, h/2+a2, fill="blue", tags=ascii_uppercase[i])
        canvas.create_text(x, h/2, text=ascii_uppercase[i], font="times 20", fill="white", tags=ascii_uppercase[i])
        x += a1 * 2 + 10

def davac(e):
    global viac
    p = canvas.gettags("current")[0]
    if p == puknuty:
        canvas.delete("all")
        canvas.create_text(w/2, h/2, text="Gratulujem, označil si puknutý tanier!", font="tims 30", fill="blue")
        canvas.create_text(w/2, h - 50, text="Viackrát si klikol na taniere: {}".format("".join(sorted(viac))), font="times 30", fill="red")
    else:
        if p not in viac:
            viac.append(p)

import tkinter as tk, random

w, h = 1000, 200
a1 = 45
a2 = 30
puknuty = ascii_uppercase[random.randint(0,9)]
viac = []

win = tk.Tk()

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()
kresli_taniere()
print(puknuty)
canvas.bind("<Button-1>", davac)

win.mainloop()

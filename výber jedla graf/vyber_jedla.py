def kresli():
    global stvorce
    a = 100
    x = 40
    for i in range(4):
        stvorce.append(canvas.create_rectangle(x, h/2, x+a, h/2+a, fill=farby[i], outline=farby[i], tags=farby[i]))
        x += 110
    canvas.create_text(w/2, 100, text='VÝBER JEDLA', font='times 40', fill='red')

def makaj(e):
    global fw
    x = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if len(x) != 0 and x[0] in stvorce:
        farba = canvas.gettags("current")[0]
        kodik = entry.get()
        if kodik != "":
            fw = open("vyber_jedla.txt", "a")
            fw.write("{} {}\n".format(kodik, f[farba]))
            fw.close()

import tkinter as tk

fw = open("vyber_jedla.txt", "w")
fw.close()
farby = ["green", "red", "blue", "orange"]
w, h = 500, 300
f = {"green": "z", "red": "c", "blue": "m", "orange": "o"}
stvorce = []

win = tk.Tk()

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()

kresli()

canvas.bind("<Button-1>", makaj)

label = tk.Label(text='kód študenta:', font="times 12")
label.pack()
entry = tk.Entry(win)
entry.pack()

win.mainloop()

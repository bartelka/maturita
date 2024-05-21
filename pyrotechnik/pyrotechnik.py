w, h = 500, 200

farby = ["green", "red", "blue", "yellow", "orange"]

px, py, = 75, 100
dlzka = 300
hrubka = 10
cas = 60

def vykresli():
    y = py
    for i in range(5):
        canvas.create_rectangle(px, y, px + dlzka, y + hrubka, fill=farby[i], tag=farby[i])
        y += hrubka
    canvas.create_text(px + dlzka + 30, 125, text=cas,  fill="red", font="times 35", tag="time")
    canvas.create_text(w/2, 50, text="Pyrotechnik", font="times 30", fill="blue")
    canvas.create_text(w/2, 75, text="označ správny káblik", font="time 13")

def casovac():
    global cas
    cas -= 1
    canvas.itemconfig("time", text=cas)
    if cas == 0:
        canvas.delete("all")
        return
    if status:
        canvas.after(200, casovac)

def cekuj(e):
    global status
    if canvas.gettags("current")[0] == kablik:
        canvas.create_text(w/2, h-25, text="Vyhral si!", font="times 35")
        status = False

import tkinter as tk, random
win = tk.Tk()

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()

kablik = random.choice(farby)
status = True

vykresli()
casovac()

canvas.bind("<Button-1>", cekuj)
win.mainloop()

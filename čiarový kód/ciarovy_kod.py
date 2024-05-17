import tkinter as tk, random

kodiky = [riadok.strip() for riadok in open("ciarovy_kod_1.txt", "r").readlines()]
def ciarovy_kod(kodik, x, y1, y2):
    x1 = x
    p = (w/2 - 10)/8
    for i in range(len(kodik)):
        if i == 0 or len(kodik) - 1 == i:
            canvas.create_rectangle(x, y1, x + int(kodik[i])*2, y2, fill="black")
        else:
            canvas.create_rectangle(x, y1, x + int(kodik[i])*2, y2 - 20, fill="black")
        x += p
    canvas.create_text((x1 + x) / 2, y2 - 10, text=kodik, font="Arial 15")

def kresli(e):
    global kodiky, status
    if status:
        canvas.delete("all")
        for i in range(4):
            kodik = kodiky.pop()
            if i < 2:
                x = 0
            else:
                x = w/2
            if i == 0 or i == 2:
                y1 = 0
            else:
                y1 = h/2
            ciarovy_kod(kodik, x, y1 + 20, y1 + h/2)
            if len(kodiky) == 0:
                status = False
                return

def kod():
    kod = ""
    for i in range(8):
        kod += str(random.randrange(1,10))
    return kod

status = True

win = tk.Tk()

w, h = 400, 400

canvas = tk.Canvas(width=w, height=h, background="white")
canvas.pack()

ciarovy_kod(kod(), 0, 0, h/2)

canvas.bind_all('<space>', kresli)

win.mainloop()

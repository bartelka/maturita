def cb():
    global status
    status = True
    canvas.delete(("all"))
    farby()

def farby():
    y = 0
    for riadok in riadky:
        farby = []
        r = [riadok[i:i+2] for i in range(0, len(riadok), 2)]
        for i in r:
            farba = int(i, 16)
            farby.append(farba)
        for i in range(len(farby)):
            if status:
                if farby[i] < 128:
                    farba = 0
                else:
                    farba = 255
            else:
                farba = farby[i]
            farba = '#%02x%02x%02x' % (farba, farba, farba)
            canvas.create_rectangle(i, y, i, y, fill=farba, outline=farba)
        y += 1

sv = open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8").readline().strip().split()
riadky = [riadok.strip() for riadok in open("ciernobiely_obrazok_1.txt", "r", encoding="utf-8").readlines()[1:]]

import tkinter as tk

status = False
w, h = int(sv[0]), int(sv[1])

win = tk.Tk()

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()

button = tk.Button(text="len čierna a biela", command=cb)
button.pack()

farby()

win.mainloop()

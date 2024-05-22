import random
slovicka = [slovicko.strip() for slovicko in open("obesenec.txt", "r", encoding="utf-8")]
hs = [i for i in random.choice(slovicka)]
h = ["."] * len(hs)

def hadaj():
    slovo = input("{}\nhádaj slovo: ".format("".join(h)))
    for i in slovo:
        if i in "".join(hs):
            h[hs.index(i)] = i

for i in range(10):
    hadaj()
    if h == hs:
        print("".join(h))
        print("Uhádol si slovo, gratulujem!")
        break

if h != hs:
    print("Premrhal si počet pokusov, slovo si neuhádol :(")

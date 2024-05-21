# Vytvorte program na učenie sa slovíčok v textovom režime s vlastnosťami:
# Program prečíta všetky slovíčka do pamäte. Hráč si vyberie, či má program zadávať slovenské alebo
# anglické slovo.
# Program postupne zadá všetky slovíčka poďla výberu zadaného jazyka a prečíta odpoveď.
# Keď slovo zadáme nesprávne, program nás ho po vyskúšaní všetkých slov, ktoré nás mal vyskúšať,
# opätovne vyskúša.
# Program nás skúša slovíčka, až kým nezadáme správne všetky slovíčka v súbore, v závere nám vypíše
# počet nesprávnych odpovedí.
slovicka = [riadok.strip() for riadok in open("ucenie_sa_slovicok.txt", "r", encoding="utf-8").readlines()]
slovenske = [slovicka[i] for i in range(len(slovicka)) if i % 2 == 0]
anglicke = [slovicka[i] for i in range(len(slovicka)) if i % 2 == 1]
aas = input("zadavat anglicky - a / slovensky - s: ")

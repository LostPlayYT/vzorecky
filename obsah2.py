print("Vítejte v apliakco pro výpočet obsahu obdelníka")
#Deklarace proměních a přetypovaní na str
a = int(input("Zadejte délku: "))
b = int(input("Zadejte šířku: "))
#Kontrolujeme záporné číslo
if a>0 and b>0:
    print("Výsledek je: ")
    print(a*b)
#Pokud nebude platit první podmínka, spíše else
else:
    print("Chyba")
#Uživatele přivítáme v aplikaci
print ("Vítejte v aplikaci pro výpočet obsahu kruhu")
#Deklarace proměných a přetypování na str
a = str(input("Zadejte poloměr: "))
#Kontrolujeme záporná čísla
if a>0:
    print("Výsledek je: ")
    print(3.14*(a*a))
#Pokud nebude platit první 
else:
    print ("Chyba")
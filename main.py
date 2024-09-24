#1. proměná s jmenem
jmeno = "Richard"

#2. proměná s přijměním
prijmeni = "Pavelek"

#3. vypsání jmena a přijmení
print(jmeno,prijmeni)

#4. vstup uživatele pro zadání věku
vek=int(input("Zadejte věk:"))
print(vek)

#5. sečtění 1. a 2. proměnné
print(len(jmeno+prijmeni))

#6. proměnná s číslem 6
cislo1 = 6

#7. cyklus přičítání hodnoty
for cislo1 in range(5):
    cislo1 += 3

#8. vypsaní cyklu
print(cislo1)

#9.požadavek pro zadání věku
input_vek = input("Zadejte věk: ")
#zkontroluje zda je zadáno celočíselná hodnota
if input_vek.isdigit():
    vek = int(input_vek)
    print("Děkuji")
else:
    #pokud je zadáno necelé číslo nebo písmena
    print("Zadej jen celočíselnou hodnotu.")

#10.
#funkce pro generování náhodných čísel
import random

#vygenerije náhodné číslo mezi 1 a 10
nahodne_cislo = random.randint(1, 10)

#vypíše náhodné číslo
print(nahodne_cislo)

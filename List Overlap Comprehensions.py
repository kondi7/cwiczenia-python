# CEL: napisz program, który zwróci listę zawierającą tylko te elementy, które są wspólne dla list (bez duplikatów).
# Upewnij się, że Twój program działa na dwóch listach o różnych rozmiarach.

import random

while True:
    try:
        do1 = int(input("Wpisz ilość elementów pierwszej listy od 0 do: "))
        ilosc_elementow1 = int(input("Wpisz ile ma zostać losowo wybranych elementow listy1: "))
        do2 = int(input("Wpisz ilość elementów drugiej listy od 0 do: "))
        ilosc_elementow2 = int(input("Wpisz ile ma zostać losowo wybranych elementow listy2:  "))

        if ilosc_elementow1 == ilosc_elementow2:
            print("Listy mają ten sam rozmiar")

        a = random.sample(range(do1), ilosc_elementow1)
        b = random.sample(range(do2), ilosc_elementow2)

        c = [i for i in a for f in b if i == f]
        print("Wspólne elementy obu list to: ", c)
        break

    except ValueError:
        print("Ilość elementów w liście nie może być mniejsza od ilości elementów losowo wybieranych")

# CEL: napisz program, który zwróci listę zawierającą tylko te elementy, które są wspólne dla tych list

import random

lista1 = []
lista2 = []
lista3 = []

for i in range(0, 200):
    liczby = random.randint(1, 500)
    liczby2 = random.randint(1, 500)
    lista1.append(liczby)
    lista2.append(liczby2)
    if liczby in lista2:
        lista3.append(liczby)
print("Wspólne liczby z listy1 i listy2 to:", lista3)

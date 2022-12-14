# Napisz program (funkcję!), który pobiera listę i zwraca nową listę zawierającą wszystkie elementy pierwszej listy
# minus wszystkie duplikaty.
# Dodatki: Napisz dwie różne funkcje, aby to zrobić - jedną używającą pętli i konstruującą listę, a drugą używającą
# zbiorów.

import random

lista1 = []


def get_lista(x, y):
    for i in range(x, y):
        a = random.randint(x, y)
        lista1.append(a)
    return lista1


def get_set():
    return set(lista1)


print(get_lista(1, 555))
print(list(get_set()))

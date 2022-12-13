# CEL: Napisz program, który pobiera listę liczb (na przykład a = [5, 10, 15, 20, 25]) i tworzy nową listę tylko z
# pierwszego i ostatniego elementu podanej listy. Dla praktyki napisz ten kod wewnątrz funkcji.

import random

a = random.sample(range(500), 5)


def nowa_lista(lista):
    return [lista[0], lista[-1]]


print(nowa_lista(a))

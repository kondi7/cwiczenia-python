# CEL: WYŚWIETL WSZYSTKIE ELEMENTY LISTY < 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for element in a:
    if element < 5:
        b.append(element)
print(b)

liczba = int(input("Wpisz liczbe: "))

for e in a:
    if e < liczba:
        c.append(e)
print(c)

# CEL: Napisz jedną linię Pythona, która bierze tę listę a i tworzy nową listę zawierającą tylko parzyste elementy
# tej listy.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [element for element in a if element % 2 == 0]
print(b)

# for x in a:
#     if x % 2 == 0:
#         b.append(x)

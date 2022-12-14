# CEL: Napisz program, który zapyta użytkownika, ile liczb Fibonnaciego ma wygenerować, a następnie je wygeneruje.
# Skorzystaj z okazji, aby pomyśleć o tym, jak możesz używać funkcji. Pamiętaj, aby poprosić użytkownika o wprowadzenie
# liczby liczb w sekwencji do wygenerowania. (Wskazówka: Ciąg Fibonnaciego to ciąg liczb, w którym następna liczba w
# sekwencji jest sumą dwóch poprzednich liczb w sekwencji. Sekwencja wygląda to tak: 1, 1, 2, 3, 5, 8, 13, …)

def ilosc_liczb(liczba):
    if liczba > 0:
        x = 1
        y = 1
        for i in range(1, liczba + 1):
            suma = x + y
            print(suma, "=", x, "+", y)
            y = x
            x = suma


print(ilosc_liczb(5))

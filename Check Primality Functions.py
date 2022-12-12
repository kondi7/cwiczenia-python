# CEL: Zapytaj użytkownika o liczbę i określ, czy jest to liczba pierwsza, czy nie.

from math import sqrt


def get_pierwsza(x):
    return int(input(x))


while True:
    liczba = get_pierwsza("Podaj liczbę by sprawdzić czy to liczba pierwsza: ")

    if liczba > 1:
        a = [i for i in range(2, int(sqrt(liczba + 1))) if liczba % i == 0]
        if len(a) == 0:
            print(liczba, "jest liczbą pierwszą")
        else:
            print(liczba, "jest liczbą złożoną")

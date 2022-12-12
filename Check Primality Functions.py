# CEL: Zapytaj użytkownika o liczbę i określ, czy jest to liczba pierwsza, czy nie.

def get_pierwsza(x):
    return int(input(x))


while True:
    liczba = get_pierwsza("Podaj liczbę by sprawdzić czy to liczba pierwsza: ")
    # a = [i for i in range(2, liczba) if liczba > 0 if liczba % i == 0]
    b = []
    if liczba > 0:
        for i in range(2, liczba):
            if liczba % i == 0:
                b.append(i)
                if len(b) == 1:
                    print(liczba, "nie jest liczba pierwsza")
                    break
                elif len(b) == 0:
                    print(liczba, "jest liczba pierwsza")
                    break

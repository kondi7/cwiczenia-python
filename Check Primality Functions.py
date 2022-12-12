# CEL: Zapytaj użytkownika o liczbę i określ, czy jest to liczba pierwsza, czy nie.

def get_pierwsza(x):
    return int(input(x))


while True:
    liczba = get_pierwsza("Podaj liczbę by sprawdzić czy to liczba pierwsza: ")
    a = [i for i in range(2, liczba) if liczba > 0 if liczba % i == 0]

    if len(a) == 0:
        print(liczba, "to liczba pierwsza")
        break
    else:
        print(liczba, "nie jest liczbą pierwszą lub jest mniejsza od zera")

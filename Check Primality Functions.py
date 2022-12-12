# CEL: Zapytaj użytkownika o liczbę i określ, czy jest to liczba pierwsza, czy nie.

def get_pierwsza(x):
    return int(input(x))


while True:
    liczba = get_pierwsza("Podaj liczbę by sprawdzić czy to liczba pierwsza: ")
    # a = [i for i in range(2, liczba) if liczba > 0 if liczba % i == 0]
    b = []
    c = [1, liczba]
    if liczba > 1:
        for i in range(1, liczba + 1):
            if liczba % i == 0:
                b.append(i)
                print(b)
                if len(b) > 2:
                    print(liczba, "nie jest liczba pierwsza")
                    break
                elif b == c:
                    print(liczba, "jest liczba pierwsza")
                    break


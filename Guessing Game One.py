# CEL: Wygeneruj losową liczbę od 1 do 9 (włączając 1 i 9). Poproś użytkownika, aby odgadł liczbę, a następnie powiedz,
# czy zgadł za mało, za dużo, czy dokładnie.

import random

losowa_liczba = random.randint(1, 20)

a = 0

while True:
    odp = int(input("Odgadnij liczbe miedzy 1 a 20: "))

    if odp == losowa_liczba and odp in range(1, 20):
        print("Zgadłeś za", a, "razem. Ta liczba to:", losowa_liczba)
        break
    elif odp < losowa_liczba and odp in range(1, 20):
        print("Za mało. Spróbuj ponownie.")
        a += 1
    elif odp > losowa_liczba and odp in range(1, 20):
        print("Za dużo. Spróbuj ponownie.")
        a += 1
    else:
        print("Wpisałeś liczbe z poza zakresu. Spróbuj ponownie")
    if 3-a == 0:
        print("Straciłes wszystkie szanse. Zagraj ponownie.")
        break

    print("Pozostało Ci", 3 - a, "szans")

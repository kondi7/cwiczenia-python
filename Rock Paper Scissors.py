# CEL: Stwórz dwuosobową grę w papier-kamień-nożyce. (Wskazówka: zapytaj o zagrania graczy (używając danych wejściowych)
# , porównaj je, wydrukuj wiadomość z gratulacjami dla zwycięzcy i zapytaj, czy gracze chcą rozpocząć nową grę)

while True:
    gracz1 = input("Gracz1 wpisz swój wybór: ")
    gracz2 = input("Gracz2 wpisz swój wybór: ")
    pula_wyborow = ["kamien", "papier", "nozyce"]

    while not gracz1 in pula_wyborow:
        gracz1 = input("Gracz1 wpisz swój wybór: ")
    while not gracz2 in pula_wyborow:
        gracz2 = input("Gracz2 wpisz swój wybór: ")

    if gracz1 == "kamien" and gracz2 == "nozyce":
        print("gracz1 wygrywa")
    elif gracz1 == "papier" and gracz2 == "kamien":
        print("gracz1 wygrywa")
    elif gracz1 == "nozyce" and gracz2 == "papier":
        print("gracz1 wygrywa")
    elif gracz1 == gracz2:
        print("remis")
    else:
        print("Gracz2 wygrywa")

    while True:
            nowa_gra = input("Zacząć od nowa? (y/n): ")
            if nowa_gra in ("y", "n"):
                break
            print("nieprawidlowy input")
    if nowa_gra == "y":
        continue
    elif nowa_gra == "n":
        break

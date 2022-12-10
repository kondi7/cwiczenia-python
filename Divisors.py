# CEL: STWÓRZ PROGRAM, KTÓRY WYŚWIETLA LISTE WSZYSTKICH DZIELNIKÓW LICZBY UŻYTKOWNIKA

liczba = int(input("Wpisz liczbę: "))
lista_dzielnikow = []
dzielniki = range(1, liczba+1)

for element in dzielniki:
    if liczba % element == 0:
        lista_dzielnikow.append(element)
print("Dzielniki Twojej liczby to:", lista_dzielnikow)

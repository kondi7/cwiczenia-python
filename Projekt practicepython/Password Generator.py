# Napisz generator haseł w Pythonie. Bądź kreatywny w sposobie generowania haseł — silne hasła składają się z małych
# i wielkich liter, cyfr i symboli. Hasła powinny być losowe, generując nowe hasło za każdym razem, gdy użytkownik
# poprosi o nowe hasło. Dołącz swój kod wykonawczy do metody main.
# Dodatek: Zapytaj użytkownika, jak silne ma być jego hasło. W przypadku słabych haseł wybierz słowo lub dwa z listy.

import random
import string

lista_hasel = ["test1", "test2", "test3", "test4"]


def main(litery, liczby, znaki):
    alfabet = random.sample(string.ascii_letters, litery)
    cyfry = random.sample(range(99), liczby)
    buba = [str(i) for i in cyfry]
    znaki_specjalne = random.sample(string.punctuation, znaki)
    kombinacja = alfabet + buba + znaki_specjalne
    random.shuffle(kombinacja)
    haslo = "".join(kombinacja)
    print("Wygenerowane haslo to:", haslo)


def how_strong_password(haslo):
    if haslo == "slabe":
        random.shuffle(lista_hasel)
        print("Twoje haslo to: ")
        return "".join(random.choice(lista_hasel))
    elif haslo == "silne":
        while True:
            try:
                a = int(input("Wprowadź ile liter ma mieć Twoje hasło < 52: "))
                b = int(input("Wprowadź ile losowych liczb ma mieć Twoje hasło < 99: "))
                c = int(input("Wprowadź ile znaków specjalnych ma mieć Twoje hasło < 32: "))
                main(a, b, c)
                break
            except ValueError:
                print("Hasło ma więcej niż ", len(string.ascii_letters), "litery lub więcej niż 99 cyfr lub więcej niż",
                      len(string.punctuation), "znaków specjalnych")
    else:
        print("Hasło musi być silne lub słabe")


how_strong_password(input("Wprowadź sile hasła. silne/slabe: "))

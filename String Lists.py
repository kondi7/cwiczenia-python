# CEL: Poproś użytkownika o string i wydrukuj, czy ten ciąg jest palindromem, czy nie. (Palindrom to string,
# który czyta to samo w przód i w tył.)

string_uzytkownika = input("Wpisz swoj string: ")
lista_w_przod = []

for i in string_uzytkownika:
    lista_w_przod.append(i)
if lista_w_przod == lista_w_przod[::-1]:
    print("to palindrom")
else:
    print("to nie jest palindrom")
# if string_uzytkownika == string_uzytkownika[::-1]:
#     print("palindrom")

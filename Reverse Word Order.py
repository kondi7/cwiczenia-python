# CEL: Napisz program (za pomocą funkcji!), który prosi użytkownika o podanie długiego łańcucha zawierającego wiele
# słów. Wydrukuj użytkownikowi ten sam ciąg, z wyjątkiem słów w odwrotnej kolejności.

def get_reversed_string(slowo):
    return ' '.join(slowo.split()[::-1])


def reverse_v1(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0, word)
        print(result)
    return " ".join(result)


print(reverse_v1("1 2 3 4 5 6"))
print(get_reversed_string("elo 1 2 3 siema"))

# def get_string(x):
#     string = x
#     result = string.split()
#     return result[::-1]
# print(get_string("a b c d e f g h "))

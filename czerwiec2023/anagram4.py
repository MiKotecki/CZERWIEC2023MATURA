def suma_roznych_cyfr(liczba):
    liczba = str(liczba)
    liczby_uzyte = []
    suma_roznych = 0
    for cyfra in liczba:
        if cyfra not in liczby_uzyte:
            suma_roznych += int(cyfra)
            liczby_uzyte.append(cyfra)

    return suma_roznych


with open("anagram.txt") as f:
    lista_dec = [int(line.strip(), 2) for line in f]

liczby_bez_0 = [x for x in lista_dec if str(x).count("0") == 0]
print(len(liczby_bez_0))

lista_sum_roznych_cyfr = [suma_roznych_cyfr(x) for x in lista_dec]

maks = max(lista_sum_roznych_cyfr)
indeks = lista_sum_roznych_cyfr.index(maks)
print(lista_dec[indeks])





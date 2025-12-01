Liczba_dodan = 0
def iloczyn(x, y):
    global Liczba_dodan
    if y == 1:
        liczna_dodan = 0
        return x
    else:
        k = y // 2
        z = iloczyn(x, k)
        if y % 2 == 0:
            Liczba_dodan += 1
            return z + z
        else:
            Liczba_dodan += 2
            return x + z + z


print(iloczyn(112, 112))
print(Liczba_dodan)
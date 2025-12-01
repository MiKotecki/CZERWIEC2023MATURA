
def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i-1] == s[j-1]:
            i += 1
            j += 1
        else:
            if s[i-1] < s[j-1]:
                return True
            else:
                return False

    if j <= n:
        return True
    else:
        return False

def sortuj_sufiksy(n, s):
    T = list(range(1, n + 1))

    for i in range(n - 1):
        for j in range(n - 1 - i):
            k1 = T[j]
            k2 = T[j + 1]

            if not czy_mniejszy(n, s, k1, k2):
                T[j], T[j + 1] = T[j + 1], T[j]

    return T

with open("sufiks_4.txt") as f:
    lista = [line.strip().split() for line in f]

    for wyrazenie in lista:
        t = sortuj_sufiksy(int(wyrazenie[0]), wyrazenie[1])
        szukany_sufiks = int(t[0]-1)
        print(szukany_sufiks)
        print(wyrazenie[1][szukany_sufiks:])


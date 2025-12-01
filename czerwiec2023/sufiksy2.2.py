
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

with open("slowa3.txt") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
    k1, k2 = f.readline().strip().split()
    k1, k2 = int(k1), int(k2)

print(czy_mniejszy(n, s, k1, k2))
print(n, s, k1, k2)

# slowa1 - True (Tak)
# slowa2 - False (Nie)
# slowa3 - False (Nie)

with open("anagram.txt") as f:
    lista_dec = [int(line.strip(), 2) for line in f]

roznice = []
for i in range(len(lista_dec)-2):
    roz_bezwzgl = abs(lista_dec[i] - lista_dec[i+1])
    roznice.append(roz_bezwzgl)

print(bin(max(roznice))[2:])

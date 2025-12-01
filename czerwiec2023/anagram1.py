
with open("anagram.txt") as f:
    lista = [line.strip() for line in f]

zrownowazone = [line for line in lista if line.count("0") == line.count("1")]
prawie_zrownowazone = [line for line in lista if abs(line.count("0") - line.count("1")) == 1]

print(len(zrownowazone))
print(len(prawie_zrownowazone))

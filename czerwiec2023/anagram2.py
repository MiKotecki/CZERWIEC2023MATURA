
with open("anagram.txt") as f:
    lista = [line.strip() for line in f]

osmio_cyfrowe = [line for line in lista if len(line) == 8]
o_najw_liczb_anagr = [line for line in osmio_cyfrowe if line.count("1") == 4 or line.count("1") == 5]

for x in o_najw_liczb_anagr:
    print(x)

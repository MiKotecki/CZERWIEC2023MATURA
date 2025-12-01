
x = 9
y = 5

z = 0
while y > 0:
    if y % 2 == 1:
        z = z + x
    x = x + x
    y = y // 2

print(z)
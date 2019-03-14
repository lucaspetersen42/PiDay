precision = 100000
sum = 0
for number in range(1, precision):
    term = (1 / (number ** 2))
    sum += term
    pi = ((sum * 6) ** (1/2))
print(pi)

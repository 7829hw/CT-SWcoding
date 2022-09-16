x = [1, 3, 5, 7, 9]
for i in range(len(x)):
    print(i, end = " ")
print()
for i in range(len(x)):
    print(x[i], end = " ")
print()
for i in range(len(x)):
    print(x[i]**2, end = " ")
print()
print(list(map(lambda a: a**2, x)))
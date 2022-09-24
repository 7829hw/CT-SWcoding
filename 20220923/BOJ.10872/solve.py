import sys


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# n = 100
# print(fact(100))


# print(sys.getrecursionlimit())
sys.setrecursionlimit(10**5)
n = 1000
print(fact(n))

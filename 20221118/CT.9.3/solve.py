import math

RtoA = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

AtoR = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def to_arabic(r):
    n = 0
    for i in range(len(r)):
        if i < len(r) - 1 and RtoA[r[i]] < RtoA[r[i + 1]]:
            n -= RtoA[r[i]]
        else:
            n += RtoA[r[i]]
    return n


def to_roman(a):
    nums = list(AtoR.keys())
    strs = list(AtoR.values())
    r = ""
    for i in range(len(AtoR)):
        while a >= nums[i]:
            r += strs[i]
            a -= nums[i]
    return r


def isPrime(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def findPrimes(n):
    primes = []
    for i in range(2, n + 1):  # for i in range(2, (n//2)+1) 로 개선 가능
        if isPrime(i):
            primes.append(i)
    return primes


prime = findPrimes(999)
num = to_arabic(input())
i = 0
while num > 1:
    if num % prime[i] == 0:
        num /= prime[i]
        print(to_roman(prime[i]))
    else:
        i += 1

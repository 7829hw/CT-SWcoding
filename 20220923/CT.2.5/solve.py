def F(N):
    if N <= 1:
        return N
    else:
        return F(N - 1) + F(N - 2)

N = int(input())
print(F(N))
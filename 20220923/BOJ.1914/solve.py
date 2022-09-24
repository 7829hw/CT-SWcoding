def hanoi(M, src ,dst, via):
    if M > 0:
        hanoi(M - 1, src, via, dst)
        print(src, '->', dst)
        hanoi(M - 1, via, dst, src)

N = 10
hanoi(N, 'A', 'B', 'C')
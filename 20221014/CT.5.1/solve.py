def solve(low, high):
    while low <= high:
        mid = (low + high) // 2
        if mid < X:
            low = mid + 1
            print(mid, "UP")
        elif mid > X:
            high = mid - 1
            print(mid, "DOWN")
        else:
            print(mid, "END")
            break

N, M = map(int, input().split())
X = int(input())

solve(N, M)
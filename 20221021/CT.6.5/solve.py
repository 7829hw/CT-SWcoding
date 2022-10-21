def findMaxBitonic(arr, low, high):
    if high < 3:
        return -1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            low = mid + 1
        elif arr[mid] < arr[mid - 1] and arr[mid + 1] < arr[mid]:
            high = mid - 1
    return -1

def solve(arr, N):
    answer = findMaxBitonic(arr, 0, N - 1)
    print(answer)



N = int(input())
array = [int(input()) for _ in range(N)]
solve(array, N)
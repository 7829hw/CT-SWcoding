import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

nums.sort(key = lambda x: (len(str(x)), -x))

print(" ".join(map(str, nums)))
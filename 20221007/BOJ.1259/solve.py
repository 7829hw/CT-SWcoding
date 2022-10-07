N = int(input())
print(list(str(N)))
print(list(str(N)[::-1]))
if list(str(N)) == list(str(N)[::-1]):
    print("palindrome")
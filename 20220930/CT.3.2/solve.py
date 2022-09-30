DIFF = ord('a') - ord('A')

# Let solve() return merged list
def solve(s, t):
    result = []
    i = 0
    j = 0
    while(i < len(s) and j < len(t)):
        if ord(t[j]) - ord(s[i]) > DIFF:
            result += [s[i]]
            i += 1
        else :
            result += [t[j]]
            j += 1
    
    if i < len(s):
        for i in range(i, len(s)):
            result += [s[i]]
    if j < len(t):
        for j in range(j, len(t)):
            result += [t[j]]

    return result

S, T = input().split()
S = sorted(list(S.upper()))
T = sorted(list(T.lower()))
print(" ".join(solve(S, T)))

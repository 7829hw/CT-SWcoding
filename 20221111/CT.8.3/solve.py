def push(stack, element):
    stack.append(element)


def pop(stack):
    if len(stack) == 0:
        return None
    return stack.pop()


def empty(stack):
    return len(stack) == 0


def top(stack):
    if empty(stack):
        return None
    return stack[-1]


def stacksort(N, order):
    stack = []
    parking = []
    cnt = 0
    s = []
    for i in range(1, N + 1):
        s.append(i)

    while cnt < N:
        if s and s[0] == order[cnt]:
            parking.append(s.pop(0))
            cnt += 1
        elif not empty(stack) and stack[-1] == order[cnt]:
            parking.append(stack.pop())
            cnt += 1
        elif s:
            stack.append(s.pop(0))
        else:
            # print(parking)
            return "no"
    # print(parking)
    return "yes"


N, M = map(int, input().split())
for _ in range(M):
    order = list(map(int, input().split()))
    print(stacksort(N, order))

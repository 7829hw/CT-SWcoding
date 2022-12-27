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


def solve(S):
    cnt = 0
    stack = []
    for i in S:
        if i == "(":
            push(stack, i)
        else:
            if empty(stack):
                cnt += 1
            pop(stack)
    return cnt + len(stack)


S = list(input())
print(solve(S))

def push(stack, element):
    stack.append(element)


def pop(stack):
    if len(stack) == 0:
        return -1
    return stack.pop()


def solve(A):
    stack = []
    for i in A:
        while True:
            temp = pop(stack)
            if temp > i or temp == -1:
                break
        if temp != -1:
            push(stack, temp)
        push(stack, i)

    return stack


N = int(input())
A = list(map(int, input().split()))
print(" ".join(map(str,solve(A))))

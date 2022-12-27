def enqueue(queue, element):
    queue.append(element)


def dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)


def empty(queue):
    return len(queue) == 0


def solve(S):
    for i in range(len(S)-1):
        dequeue(S)
        temp = dequeue(S)
        enqueue(S, temp)
        # print(S)
    print(dequeue(S))

N = int(input())
S = list(range(1, N + 1))
solve(S)
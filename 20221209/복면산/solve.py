from itertools import permutations


def to_int(word, DICT):
    value = 0
    for char in word:
        value = value * 10 + DICT[char]
    return value


def is_valid(w1, w2, w3, DICT):
    a = to_int(w1, DICT)
    b = to_int(w2, DICT)
    c = to_int(w3, DICT)
    return a + b == c


def solve(w1, w2, w3):
    letters = set(w1 + w2 + w3)
    numbers = list(range(10))
    if len(letters) > 10:
        return False  # 문자가 10개 이상이면 솔루션이 없음
    for perm in permutations(numbers, len(letters)):
        DICT = dict(zip(letters, perm))  # 딕셔너리 생성
        if is_valid(w1, w2, w3, DICT):
            return True  # 하나라도 조건이 만족하면 True 리턴
    return False


w1, w2, w3 = input().split()
print("YES" if solve(w1, w2, w3) else "NO")

import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())


def D(x):
    return x * 2 % 10000


def S(x):
    if x == 0:
        return 9999
    else:
        return x - 1


def L(x):
    x1, x2, x3, x4 = x // 1000, (x % 1000) // 100, (x % 100) // 10, x % 10
    return x2 * 1000 + x3 * 100 + x4 * 10 + x1


def R(x):
    x1, x2, x3, x4 = x // 1000, (x % 1000) // 100, (x % 100) // 10, x % 10
    return x4 * 1000 + x1 * 100 + x2 * 10 + x3


while T:
    T -= 1
    A, B = map(int, input().split())
    items = [D, S, L, R]
    ch = [0] * 10001
    queue = deque()
    queue.append([A, ""])
    while queue:
        tmp, ans = queue.popleft()
        if tmp == B:
            print(ans)
            break
        for item in items:
            func = item.__name__
            cal = item(tmp)
            if ch[cal] == 0:
                ch[cal] = 1
                queue.append([cal, ans+func])

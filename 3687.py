import sys
# sys.stdin = open("input.txt", "r")

INF = 999999999999999999999999999999999999999999999999999

dy = [INF for _ in range(101)]
dy[2] = 1, dy[3] = 7, dy[4] = 4, dy[5] = 2, dy[6] = 0, dy[7] = 8


def go(x):
    if x <= 1:
        return dy[x]
    if dy[x] != INF:
        if x == 6:
            return 6
        return dy[x]
    else:
        for i in range(2, 8):
            tmp = go(x-i)
            dy[x] = min(dy[x], tmp*10 + dy[i])
    return dy[x]


n = int(input())

for _ in range(n):
    num = int(input())
    tmp = num
    maxx = 0
    minn = INF
    if num % 2 == 1:
        maxx = 7
        tmp -= 3
    while tmp:
        maxx = maxx * 10 + 1
        tmp -= 2

    print(go(num), maxx)

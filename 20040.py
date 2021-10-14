import sys
sys.stdin = open("input.txt", "r")

ans = 0
n, m = map(int, input().split())
unf = [i for i in range(n)]


def find(x):
    if x == unf[x]:
        return x
    unf[x] = find(unf[x])
    return unf[x]


def union(x, y):
    global i, ans
    x = find(x)
    y = find(y)
    if x == y:
        ans = i + 1
    else:
        if x < y:
            unf[y] = x
        else:
            unf[x] = y


for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if not ans:
        union(x, y)

print(ans)

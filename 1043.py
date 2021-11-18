import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
tp = list(map(int, input().split()))[1:]
f = [i for i in range(n+1)]
node = [[] for _ in range(m)]
ans = 0


def find(x):
    if x == f[x]:
        return x
    f[x] = find(f[x])
    return f[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        f[y] = x
    else:
        f[x] = y


for i in range(m):
    a = list(map(int, input().split()))[1:]
    node[i] = a[:]
    for i in range(len(a)-1):
        union(a[i], a[i+1])

for t in tp:
    if f[t] not in tp:
        tp.append(f[t])


for i in range(1, n+1):
    if f[i] in tp:
        tp.append(i)

for x in node:
    for y in x:
        if y in tp:
            break
    else:
        ans += 1

print(ans)

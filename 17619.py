import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
log = [[-1, -1, 0]]
parent = [i for i in range(n+1)]


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for i in range(n):
    s, e, h = map(int, sys.stdin.readline().rstrip().split())
    log.append([s, e, i+1])

log.sort(key=lambda x: (x[0], x[1]))
x, y, _ = log[1]
for i in range(2, len(log)):
    nx, ny, _ = log[i]
    if nx <= y:
        union(log[i-1][2], log[i][2])
        y = max(y, ny)
    else:
        x, y = nx, ny

for _ in range(m):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    if find(s) == find(e):
        print(1)
    else:
        print(0)

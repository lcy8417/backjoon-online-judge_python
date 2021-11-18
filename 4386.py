import sys
from heapq import heappush, heappop
from math import sqrt
sys.stdin = open("input.txt", "r")

n = int(input())
f = [i for i in range(n)]
pos = [list(map(float, input().split())) for _ in range(n)]
ans = 0
heap = []


def find(x):
    if x == f[x]:
        return x
    f[x] = find(f[x])
    return f[x]


def union(x, y):
    x = f[x]
    y = f[y]
    if x < y:
        f[y] = x
    else:
        f[x] = y


for i in range(n-1):
    for j in range(i+1, n):
        heappush(heap, (sqrt((pos[i][0] - pos[j][0])
                 ** 2 + (pos[i][1] - pos[j][1]) ** 2), i, j))

while heap:
    dis, x, y = heappop(heap)
    px, py = find(x), find(y)
    if px == py:
        continue
    union(x, y)
    ans += dis

print(ans)

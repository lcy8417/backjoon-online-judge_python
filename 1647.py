import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
unf = [i for i in range(n+1)]
ans = 0
heap = []
edge = 0


def find(x):
    if x == unf[x]:
        return x
    unf[x] = find(unf[x])
    return unf[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        unf[y] = x
    else:
        unf[x] = y


for _ in range(m):
    a, b, c = map(int, input().split())
    heappush(heap, (c, a, b))

while heap:
    c, a, b = heappop(heap)
    if edge >= n-2:
        break
    if find(a) == find(b):
        continue
    union(a, b)
    edge += 1
    ans += c

print(ans)

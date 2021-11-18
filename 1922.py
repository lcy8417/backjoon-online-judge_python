import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
m = int(input())
ans = 0
unf = [i for i in range(n+1)]
q = []


def find(x):
    if unf[x] == x:
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
    heappush(q, [c, a, b])

while q:
    cost, a, b = heappop(q)
    if find(a) == find(b):
        continue
    ans += cost
    union(a, b)

print(ans)

import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
unf = [i for i in range(n+1)]
heap = []


def find(x):
    if x == unf[x]:
        return x
    else:
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
    heappush(heap, (-c, a, b, c))

s, e = map(int, input().split())

while heap:
    _, x, y, z = heappop(heap)
    union(x, y)
    if find(s) == find(e):
        print(z)
        break

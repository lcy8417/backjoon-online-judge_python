import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 1000001


def ditra(s, e):
    dis = [INF for _ in range(n+1)]
    ch = [0 for _ in range(n+1)]
    ch[s] = 1
    heap = []
    for i in range(len(s)):
        dis[i] = field[s][i]
        if dis[i] != INF and dis[i] != 0:
            heappush(heap, (dis[i], i))

    while heap:
        cost, v = heappop(heap)
        if v == e:
            break
        if ch[v]:
            continue
        ch[v] = 1
        for k in range(1, n+1):
            nCost = cost + field[v][k]
            if dis[k] > nCost:
                dis[k] = nCost
                heappush(heap, (nCost, k))

    return dis[e]


n, m, x = map(int, input().split())
field = [[] for _ in range(n+1)]
ans = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    field[a].append((b, c))

for i in range(1, n+1):
    ans = max(ans, ditra(i, x) + ditra(x, i))

print(ans)

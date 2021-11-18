import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 200000 * 1000 + 1


def dij(s):
    global req
    heap = []
    ch = [0 for _ in range(n+1)]
    dp = [INF for _ in range(n+1)]
    dp[s] = 0
    heappush(heap, (0, s))
    while heap:
        cost, x = heappop(heap)
        if ch[x]:
            continue
        ch[x] = 1
        for nx, nCost in graph[x]:
            tot = cost + nCost
            if dp[nx] > tot:
                dp[nx] = tot
                heappush(heap, [tot, nx])
    return dp


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

a, b = map(int, input().split())

v1 = dij(a)
v2 = dij(b)
ans = min(v1[1] + v1[b] + v2[n], v2[1] + v2[a] + v1[n])
if ans >= INF:
    print(-1)
else:
    print(ans)

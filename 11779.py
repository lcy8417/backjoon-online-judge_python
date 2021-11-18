import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")

INF = 100000001
n = int(input())
m = int(input())
city = [[] for _ in range(n+1)]
dp = [INF for _ in range(n+1)]
path = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    city[a].append((b, c))

s, e = map(int, input().split())


def dij():
    ch = [0 for _ in range(n+1)]
    heap = []
    heappush(heap, (0, s))
    while heap:
        _, x = heappop(heap)
        if ch[x]:
            continue
        ch[x] = 1
        for next, nCost in city[x]:
            if dp[x] + nCost < dp[next]:
                dp[next] = dp[x] + nCost
                path[next] = x
                heappush(heap, (dp[next], next))


def dfs(x, cnt):
    if x == s:
        print(cnt)
        print(x, end=' ')
        return
    dfs(path[x], cnt+1)
    print(x, end=' ')


dp[s] = 0
dij()

print(dp[e])
dfs(e, 1)

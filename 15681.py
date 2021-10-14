import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]


def dfs(x):
    dp[x] = 1
    for next in graph[x]:
        if not dp[next]:
            dfs(next)
            dp[x] += dp[next]


for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for _ in range(q):
    print(dp[int(sys.stdin.readline())])

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

n = int(input())
dp = [[0, 0] for _ in range(n+1)]
edge = [[] for _ in range(n+1)]


def go(x):
    dp[x][0] = 1
    for next in edge[x]:
        if not dp[next][0]:
            go(next)
            dp[x][0] += min(dp[next][0], dp[next][1])
            dp[x][1] += dp[next][0]


for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

go(1)
print(min(dp[1][0], dp[1][1]))

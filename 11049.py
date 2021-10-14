import sys
sys.stdin = open("input.txt", "r")

INF = 2**31
n = int(input())
dy = [[INF for _ in range(n+1)] for _ in range(n+1)]
a = [0 for _ in range(n+1)]


def dfs(s, e):
    if e-s == 1:
        return 0
    if dy[s][e] != INF:
        return dy[s][e]
    for k in range(s+1, e):
        dy[s][e] = min(dy[s][e], dfs(s, k)+dfs(k, e)+a[s]*a[k]*a[e])
    return dy[s][e]


for i in range(n):
    a[i], a[i+1] = map(int, input().split())
    dy[i][i], dy[i][i+1] = 0, a[i]*a[i+1]

dfs(0, n)
print(dy[0][n])

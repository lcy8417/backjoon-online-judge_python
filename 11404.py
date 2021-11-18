import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 100000001
n = int(input())
m = int(input())
cost = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(cost[i][j], end=' ')
    print()

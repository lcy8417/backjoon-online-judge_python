import sys
# sys.stdin = open("input.txt", "r")

INF = 2147000000
n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dy = [INF]*(k+1)
dy[0] = 0
for x in coin:
    for i in range(x, k+1):
        if dy[i-x] != INF:
            dy[i] = min(dy[i-x]+1, dy[i])

if dy[k] == INF:
    print(-1)
else:
    print(dy[k])

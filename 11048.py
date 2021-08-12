import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dy[i][j] = max(dy[i-1][j], dy[i][j-1], dy[i-1][j-1]) + miro[i-1][j-1]

print(dy[n][m])

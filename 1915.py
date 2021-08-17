import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
square = [[0]*(m+1) for _ in range(n+1)]
answer = 0
for i in range(n):
    square[i+1][1:] = list(map(int, input()))
dy = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if square[i][j]:
            dy[i][j] = min(dy[i-1][j-1], dy[i-1][j], dy[i][j-1]) + 1
            answer = max(answer, dy[i][j])
print(answer**2)

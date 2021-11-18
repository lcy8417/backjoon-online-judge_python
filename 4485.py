import sys
from heapq import heappush, heappop
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = (125 ** 2) * 10
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
cnt = 1
while True:
    n = int(input())
    if not n:
        break
    field = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF for _ in range(n)] for _ in range(n)]
    ans = INF
    heap = []
    heappush(heap, (field[0][0], 0, 0))
    dp[0][0] = field[0][0]
    while heap:
        cost, x, y = heappop(heap)
        if x == n-1 and y == n-1:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                nextCost = cost + field[nx][ny]
                if nextCost < dp[nx][ny]:
                    dp[nx][ny] = nextCost
                    heappush(heap, (nextCost, nx, ny))
    print(f"Problem {cnt}: {dp[n-1][n-1]}")
    cnt += 1

import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
bread = [list(input()) for _ in range(n)]
ch = [[0 for _ in range(m)] for _ in range(n)]
dx, dy = [-1, 0, 1], [1, 1, 1]
ans = 0


def dfs(x, y):
    if y == m-1:
        return 1
    else:
        for k in range(3):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and bread[nx][ny] == '.':
                bread[nx][ny] = 'x'
                if dfs(nx, ny):
                    return 1
    return 0


for i in range(n):
    ans += dfs(i, 0)

print(ans)

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
dy = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
pipe = [list(map(int, input().split())) for _ in range(n)]
dy[0][1][0] = 1


def dfs(x, y, z):
    if x < 0 or y < 0 or pipe[x][y]:
        return 0
    if dy[x][y][z]:
        return dy[x][y][z]
    if z == 0:
        dy[x][y][z] = dfs(x, y-1, 2) + dfs(x, y-1, 0)
    elif z == 1:
        dy[x][y][z] = dfs(x-1, y, 1) + dfs(x-1, y, 2)
    else:
        if 0 <= x-1 and 0 <= y-1 and pipe[x-1][y] == 0 and pipe[x][y-1] == 0:
            dy[x][y][z] = dfs(x-1, y-1, 0) + \
                dfs(x-1, y-1, 1) + dfs(x-1, y-1, 2)
    return dy[x][y][z]


dfs(n-1, n-1, 0), dfs(n-1, n-1, 1), dfs(n-1, n-1, 2)
print(sum(dy[n-1][n-1]))

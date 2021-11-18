import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, 0, -1, 0], [0, 0, 0, 1, 0, -1]


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    ch = [[[-1 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    ch[x][y][z] = 0
    while q:
        x, y, z = q.popleft()
        if bd[x][y][z] == 'E':
            print(f'Escaped in {ch[x][y][z]} minute(s).')
            return
        for k in range(6):
            nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and ch[nx][ny][nz] == -1 and bd[nx][ny][nz] != '#':
                ch[nx][ny][nz] = ch[x][y][z] + 1
                q.append((nx, ny, nz))
    print('Trapped!')
    return


while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break

    bd = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    for i in range(l):
        temp = [list(input().strip()) for _ in range(r+1)]
        for j in range(r):
            bd[i][j] = temp[j]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if bd[i][j][k] == 'S':
                    bfs(i, j, k)
                    break

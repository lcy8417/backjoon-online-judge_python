import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
field = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
ch = [0 for _ in range(26)]
answer = 0
ch[field[0][0]] = 1

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and ch[field[nx][ny]] == 0:
            ch[field[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            ch[field[nx][ny]] = 0


dfs(0, 0, 1)
print(answer)


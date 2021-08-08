import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0
field = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
answer = 0
shark = {
    'x': 0,
    'y': 0,
    'size': 2,
    'cnt': 0
}

for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            shark['x'] = i
            shark['y'] = j
            field[i][j] = 0
        elif field[i][j]:
            cnt += 1

while cnt:
    ch = [[0] * n for _ in range(n)]
    queue.append([shark['x'], shark['y'], 0])
    ch[shark['x']][shark['y']] = 1
    food = []
    while queue:
        x, y, move = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0 and shark['size'] >= field[nx][ny]:
                ch[nx][ny] = 1
                queue.append([nx, ny, move+1])
                if field[nx][ny] and shark['size'] > field[nx][ny]:
                    food.append([nx, ny, move+1])
    food.sort(key=lambda g: (g[2], g[0], g[1]))
    if len(food):
        shark['x'] = food[0][0]
        shark['y'] = food[0][1]
        shark['cnt'] = shark['cnt'] + 1
        if shark['cnt'] >= shark['size']:
            shark['size'] = shark['size'] + 1
            shark['cnt'] = 0
        answer += food[0][2]
        field[shark['x']][shark['y']] = 0
    cnt -= 1

print(answer)

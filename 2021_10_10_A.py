import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx, dy = [0, 1, -1], [1, 1, 1]
T = int(input())
while T:
    T -= 1
    queue = deque()
    ans = 'NO'
    n = int(input())
    field = [list(input()) for _ in range(2)]
    field[0][0] = '1'
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        if x == 1 and y == n-1:
            ans = 'YES'
            break
        for k in range(3):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < 2 and 0 <= ny < n and field[nx][ny] == '0':
                field[nx][ny] = 1
                queue.append([nx, ny])
    print(ans)

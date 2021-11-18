import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

queue = deque()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
puzzle = [list(map(int, input().split())) for _ in range(3)]
ch = dict()
temp = ''

for i in range(3):
    for j in range(3):
        temp += str(puzzle[i][j])

queue.append(temp)
ch[temp] = 0
while queue:
    temp, a, b, cnt = queue.popleft()
    zero = temp.find('0')
    x = zero // 3
    y = zero % 3
    if temp == '123456780':
        print(ch.get(temp))
        sys.exit(0)
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < 3 and 0 <= ny < 3:
            next = 3 * nx + ny
            nextValue = list(temp)
            nextValue[next], nextValue[zero] = nextValue[zero], nextValue[next]
            nextValue = ''.join(nextValue)
            if not ch.get(nextValue):
                ch[nextValue] = ch[temp] + 1
                queue.append(nextValue)

print(-1)

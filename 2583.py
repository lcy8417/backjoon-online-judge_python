import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m, k = map(int, input().split())
paper = [[0] * m for _ in range(n)]
queue = deque()
answer = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
while k:
    lst = list(map(int, input().split()))
    for i in range(lst[1], lst[3]):
        for j in range(lst[0], lst[2]):
            paper[i][j] = 1
    k -= 1

for i in range(n):
    for j in range(m):
        if paper[i][j] == 0:
            cnt = 1
            paper[i][j] = 1
            queue.append([i, j])
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 0:
                        paper[nx][ny] = 1
                        cnt += 1
                        queue.append([nx, ny])
            answer.append(cnt)

answer.sort()
print(len(answer))
for x in answer:
    print(x, end=' ')

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n = int(input())
graph, max_height, answer = [], 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(n):
    graph.append(list(map(int, input().split())))
    max_height = max(max_height, max(graph[i]))

for h in range(0, max_height+1):
    tmp = [graph[i][:] for i in range(n)]
    tot = 0
    queue = deque()
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > h:
                tmp[i][j] = 0
                tot += 1
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and tmp[nx][ny] > h:
                            tmp[nx][ny] = 0
                            queue.append([nx, ny])
    answer = max(answer, tot)
print(answer)

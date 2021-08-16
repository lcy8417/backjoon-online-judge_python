import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())
while T:
    v, e = map(int, input().split())
    time_taken = list(map(int, input().split()))
    time_taken = [0] + time_taken
    graph = [[] for _ in range(v+1)]
    dy = [[0, 0] for _ in range(v+1)]
    queue = deque()
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        dy[y][0] += 1
    finish = int(input())
    time = 0
    for i in range(1, len(graph)):
        if dy[i][0] == 0:
            queue.append([i, time_taken[i]])

    while queue:
        x, t = queue.popleft()
        if finish == x and dy[x][0] == 0:
            print(t)
            break
        for next in graph[x]:
            dy[next][0] -= 1
            dy[next][1] = max(t + time_taken[next], dy[next][1])
            if dy[next][0] == 0:
                queue.append([next, dy[next][1]])
    T -= 1

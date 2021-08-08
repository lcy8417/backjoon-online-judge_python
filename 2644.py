import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n = int(input())
start, end = map(int, input().split())
m = int(input())
ch = [0] * (n+1)
graph = [[] for _ in range(n+1)]
queue = deque()
answer = -1
while m:
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    m -= 1

queue.append([start, 0])
ch[start] = 1
while queue:
    x, cnt = queue.popleft()
    if x == end:
        answer = cnt
        break
    for next in graph[x]:
        if ch[next] == 0:
            ch[next] = 1
            queue.append([next, cnt+1])

print(answer)

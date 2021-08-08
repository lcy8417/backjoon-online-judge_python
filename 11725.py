import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n = int(input())
node = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

node[1] = 1
queue.append(1)
while queue:
    x = queue.popleft()
    for i in range(len(graph[x])):
        next = graph[x][i]
        if node[next] == 0:
            node[next] = x
            queue.append(next)

for i in range(2, n+1):
    print(node[i])

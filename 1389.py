import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
minn = 2147000000
res = 0

for _ in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for x in range(1, v+1):
    tmp = [0] * (v+1)
    ch = [0] * (v+1)
    ch[x] = 1
    queue = deque()
    queue.append([x, 0])
    while queue:
        cur, dis = queue.popleft()
        for next in graph[cur]:
            if ch[next] == 0:
                ch[next] = 1
                tmp[next] = dis+1
                queue.append([next, dis+1])
    if minn > sum(tmp):
        minn = sum(tmp)
        res = x

print(res)

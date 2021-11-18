import sys
from collections import deque
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split()))[1:] for _ in range(m)]
graph = [[] for _ in range(n+1)]
child = [0 for _ in range(n+1)]
ans = []
q = deque()

for i in range(m):
    for j in range(len(a[i])-1):
        now, next = a[i][j], a[i][j+1]
        graph[now].append(next)
        child[next] += 1

for i in range(1, n+1):
    if child[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    ans.append(x)
    for next in graph[x]:
        child[next] -= 1
        if child[next] == 0:
            q.append(next)

if len(ans) != n:
    print(0)
else:
    for x in ans:
        print(x)

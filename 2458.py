import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
node = [0 for _ in range(n+1)]
ans = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(x):
    global older
    for next in graph[x]:
        if not ch[next]:
            ch[next] = 1
            node[next] += 1
            older += 1
            dfs(next)


for i in range(1, n+1):
    ch = [0 for _ in range(n+1)]
    ch[i] = 1
    older = 0
    dfs(i)
    node[i] += older

for i in range(1, n+1):
    if node[i] == n-1:
        ans += 1

print(ans)

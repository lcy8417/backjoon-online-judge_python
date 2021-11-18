import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = float('inf')
n, m = map(int, input().split())
graph = {i: {} for i in range(1, n+1)}
dis = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if not graph[a].get(b):
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

dis[1] = 0
for i in range(n-1):
    for node in graph:
        for next in graph[node]:
            dis[next] = min(dis[next], dis[node] + graph[node][next])

for node in graph:
    for next in graph[node]:
        if dis[next] > dis[node] + graph[node][next]:
            print(-1)
            exit(0)

for i in range(2, n+1):
    print(dis[i] if dis[i] != INF else -1)

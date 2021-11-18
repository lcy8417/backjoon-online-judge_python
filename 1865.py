import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = float('inf')
T = int(input())
while T:
    T -= 1
    n, m, w = map(int, input().split())
    graph = {i: {} for i in range(1, n+1)}
    dis = [INF for _ in range(n+1)]
    ans = 'NO'
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a].get(b):
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
        if graph[b].get(a):
            graph[b][a] = min(graph[b][a], c)
        else:
            graph[b][a] = c

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s][e] = -t
        dis[e] = 0

    for _ in range(n-1):
        for node in graph:
            for next in graph[node]:
                dis[next] = min(dis[next], dis[node] + graph[node][next])

    for node in graph:
        for next in graph[node]:
            if dis[next] > dis[node] + graph[node][next]:
                ans = 'YES'
                break
    print(ans)

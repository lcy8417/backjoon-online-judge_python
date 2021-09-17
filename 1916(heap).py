from heapq import heappush, heappop

INF = 100000001
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
d = [INF for _ in range(n+1)]
visit = [False for _ in range(n+1)]


def dijkstra(s, e):
    heap = []

    d[s] = 0
    heappush(heap, [0, s])
    while heap:
        cur = heappop(heap)[1]
        if visit[cur]:
            continue

        visit[cur] = True
        for next, dis in graph[cur]:
            cost = d[cur] + dis
            if not visit[next] and cost < d[next]:
                d[next] = cost
                heappush(heap, (cost, next))

    print(d[e])


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

s, e = map(int, input().split())

dijkstra(s, e)

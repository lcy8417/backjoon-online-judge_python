import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
node = [n for _ in range(n+1)]
s = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[b][a] = 1

for i in range(n+1):
    graph[i][i] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        node[j] -= graph[i][j]
        node[i] -= graph[i][j]
    node[i] += 1

for i in range(1, n+1):
    print(node[i])

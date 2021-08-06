import sys
sys.stdin = open("input.txt", "r")


def go(x):
    for e in range(n):
        if graph[x][e] and answer[s][e] == 0:
            answer[s][e] = 1
            go(e)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

for s in range(n):
    go(s)

for i in range(n):
    for j in range(n):
        print(answer[i][j], end=' ')
    print()

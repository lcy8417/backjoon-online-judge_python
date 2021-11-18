import sys
sys.setrecursionlimit(10**9)
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())


def dfs(x):
    global n
    ch[x] = 1
    cycle.append(x)
    next = a[x]

    if ch[next]:
        if next in cycle:
            n -= len(cycle[cycle.index(next):])
    else:
        dfs(next)


while T:
    T -= 1
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ch = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        if not ch[i]:
            cycle = []
            dfs(i)
    print(n)

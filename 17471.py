import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
pop = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(1, n+1)}
ans = float('inf')
for now in range(1, n+1):
    a = list(map(int, input().split()))
    for next in a[1:]:
        graph[now].append(next)


def isDivide(area):
    if not area:
        return False
    q = deque()
    ch = [0 for _ in range(n+1)]
    cnt = 0
    s = area[0]
    q.append(s)
    while q:
        x = q.popleft()
        if ch[x]:
            continue
        ch[x] = 1
        cnt += 1
        for next in graph[x]:
            if next in area:
                q.append(next)

    if cnt == len(area):
        return True
    else:
        return False


def dfs(x, area1, area2, pop1, pop2):
    global ans
    dif = abs(pop1 - pop2)
    if ans > dif and isDivide(area1) and isDivide(area2):
        ans = dif
    for i in range(x, n+1):
        tmp = area1[:]
        tmp.remove(i)
        dfs(i+1, tmp, area2 + [i], pop1 - pop[i], pop2 + pop[i])


dfs(1, [i for i in range(1, n+1)], [], sum(pop), 0)
print(ans if ans != float('inf') else -1)

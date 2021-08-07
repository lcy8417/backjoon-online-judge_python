import sys
sys.stdin = open("input.txt", "r")

v, e = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(e)]
root = [i for i in range(v+1)]
answer = 0
graph.sort(key=lambda g: (g[2]))


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


def union(x, y):
    if x < y:
        root[y] = x
    else:
        root[x] = y


for start, end, dis in graph:
    start_root = find(start)
    end_root = find(end)
    if start_root != end_root:
        union(start_root, end_root)
        answer += dis

print(answer)

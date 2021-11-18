import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
cut = int(input())
tree = [[] for _ in range(n)]
ch = [0 for _ in range(n)]
ans = 0


def dfs(x, y):
    global ans
    if not len(tree[x]) and not ch[x]:
        ans += y
    ch[x] = 1
    for next in tree[x]:
        if not ch[next]:
            dfs(next, y)


for i in range(n):
    if a[i] != -1 and i != cut:
        tree[a[i]].append(i)

dfs(cut, 0)

for i in range(n):
    if not ch[i]:
        dfs(i, 1)
print(ans)

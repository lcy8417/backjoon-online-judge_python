import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
ans = 0
node = 0


def go(x, sum):
    global maxx, node
    if maxx < sum:
        maxx = sum
        node = x
    for nextNode, cost in tree[x]:
        if not ch[nextNode]:
            ch[nextNode] = 1
            go(nextNode, sum+cost)


for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(1, len(a)-1, 2):
        tree[a[0]].append([a[i], a[i+1]])

for i in range(n):
    a = list(map(int, input().split()))
    for i in range(1, len(a)-1, 2):
        tree[a[0]].append([a[i], a[i+1]])

for i in range(2):
    ch = [0 for _ in range(n+1)]
    maxx = 0
    if i == 0:
        ch[1] = i
        go(1, 0)
    else:
        ch[node] = 1
        go(node, 0)

print(maxx)

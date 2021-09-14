import sys
sys.stdin = open("input.txt", "r")

n = int(input())
emp = list(map(int, input().split()))
dis = [[] for _ in range(n)]
time = [0 for _ in range(n)]
ans = 0


def go(s):
    global ans
    if len(dis[s]) == 0:
        time[s] = 0
        return

    childNode = []
    for child in dis[s]:
        go(child)
        childNode.append(time[child])

    childNode.sort(reverse=True)
    time[s] = max([childNode[i]+i+1 for i in range(len(childNode))])


for i, x in enumerate(emp):
    if x != -1:
        dis[x].append(i)

go(0)
print(time[0])

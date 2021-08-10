import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
sel = [[0] for _ in range(m)]
ans = 2147000000


def go(x, s):
    global ans
    if x == m:
        tot = 0
        for x1, y1 in house:
            tmp = 2147000000
            for x2, y2 in sel:
                tmp = min(tmp, abs(x1-x2) + abs(y1-y2))
            tot += tmp
        ans = min(ans, tot)
    else:
        for i in range(s, len(chicken)):
            sel[x] = chicken[i]
            go(x+1, i+1)


for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

go(0, 0)
print(ans)

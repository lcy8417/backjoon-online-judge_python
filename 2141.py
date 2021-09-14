import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
tot, lt = 0, 0

city.sort()
rt = city[0][1]
for i in range(1, len(city)):
    dis = city[i][0] - city[0][0]
    rt += city[i][1]
    tot += dis * city[i][1]

minn = tot
ans = city[0][0]
for i in range(1, len(city)):
    dif = city[i][0] - city[i-1][0]
    lt += city[i-1][1]
    rt -= city[i-1][1]
    tot = tot + (lt - rt) * dif
    if minn > tot:
        minn = tot
        ans = city[i][0]
    elif minn == tot:
        ans = min(city[i][0], ans)

print(ans)

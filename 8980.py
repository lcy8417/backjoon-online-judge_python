import sys
# sys.stdin = open("input.txt", "r")

n, max_w = map(int, input().split())
m = int(input())
weight = [max_w for _ in range(n+1)]
ans = 0
info = [list(map(int, input().split())) for _ in range(m)]
info.sort(key=lambda x: x[1])

for x, y, z in info:
    tmp = min(weight[x:y])
    tmp = tmp if tmp < z else z
    ans += tmp
    for i in range(x, y):
        weight[i] -= tmp

print(ans)

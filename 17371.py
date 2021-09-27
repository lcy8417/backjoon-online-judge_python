import sys
import math
sys.stdin = open("input.txt", "r")


def calc(a, b, c, d):
    return math.sqrt((a-c) ** 2 + (b-d) ** 2)


n = int(input())
pos = []
minn = 2147000000
x, y = 0, 0
for _ in range(n):
    pos.append(list(map(int, input().split())))

for x1, y1 in pos:
    maxx = 0
    px, py = 0, 0
    for x2, y2 in pos:
        tmp = calc(x1, y1, x2, y2)
        if maxx < tmp:
            maxx = tmp
    if minn > maxx:
        minn = maxx
        x, y = x1, y1

print(x, y)

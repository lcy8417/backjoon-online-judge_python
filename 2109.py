import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
ans = 0
pay = []
day = [i for i in range(10001)]


def find(x):
    if x == 0:
        return 0
    if x == day[x]:
        day[x] -= 1
        return x
    else:
        day[x] = find(day[x])
        return day[x]


for _ in range(n):
    pay.append(list(map(int, input().split())))

pay.sort(reverse=True)

for x, y in pay:
    if find(y) > 0:
        ans += x

print(ans)

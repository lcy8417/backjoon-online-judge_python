import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
ans = 0
pay = []
deadline = [i for i in range(200001)]


def find(x):
    if x == 0:
        return 0
    if x == deadline[x]:
        deadline[x] -= 1
        return x
    else:
        deadline[x] = find(deadline[x])
        return deadline[x]


for _ in range(n):
    pay.append(list(map(int, input().split())))

pay.sort(key=lambda x: -x[1])

for x, y in pay:
    if find(x) > 0:
        ans += y

print(ans)

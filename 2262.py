import sys
# sys.stdin = open("input.txt", "r")

INF = 2147000000

n = int(input())
toner = [INF] + list(map(int, input().split())) + [INF]
ans = 0

while n >= 2:
    idx = toner.index(n)
    ans += min(abs(toner[idx] - toner[idx-1]), abs(toner[idx] - toner[idx+1]))
    del toner[idx]
    n -= 1

print(ans)

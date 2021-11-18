import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 2147000000
n, m = map(int, input().split())
imp = [0 for _ in range(n+1)]
dp = [[INF for _ in range(41)] for _ in range(n+1)]
for x in list(map(int, input().split())):
    imp[x] = 1
queue = deque()
queue.append([0, 0])
dp[0][0] = 0
while queue:
    day, coupon = queue.popleft()
    for i in range(1, 6, 2):
        next = day + i
        if next > n:
            continue
        if i == 1:
            if imp[next]:
                dp[next][coupon] = min(dp[next][coupon], dp[day][coupon])
                queue.append([next, coupon])
                break
            if coupon >= 3 and dp[next][coupon-3] > dp[day][coupon]:
                dp[next][coupon-3] = dp[day][coupon]
                queue.append([next, coupon-3])
            if dp[next][coupon] > dp[day][coupon] + 10000:
                dp[next][coupon] = dp[day][coupon] + 10000
                queue.append([next, coupon])
        if i == 3 and dp[next][coupon+1] > dp[day][coupon] + 25000:
            dp[next][coupon+1] = dp[day][coupon] + 25000
            queue.append([next, coupon+1])
        if i == 5 and dp[next][coupon+2] > dp[day][coupon] + 37000:
            dp[next][coupon+2] = dp[day][coupon] + 37000
            queue.append([next, coupon+2])

print(min(dp[n]))

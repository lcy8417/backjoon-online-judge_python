import sys
import math
# sys.stdin = open("input.txt", "r")

ans = 0

n, m = map(int, input().split())
ball = list(map(int, input().split()))
lt, rt = min(ball), sum(ball)
lst = []


def groupCnt(x):
    cnt = 1
    tot = 0
    tmp = []
    ballCnt = 0
    for item in ball:
        if tot + item > x:
            cnt += 1
            tot = item
            tmp.append(ballCnt)
            ballCnt = 1
        else:
            tot += item
            ballCnt += 1
    if ballCnt:
        tmp.append(ballCnt)
    return tmp, cnt


while lt <= rt:
    mid = (lt + rt) // 2
    tmp, cnt = groupCnt(mid)
    if cnt <= m and max(ball) <= mid:
        lst = tmp
        ans = mid
        rt = mid-1
    else:
        lt = mid+1

print(ans)
while len(lst) < m:
    for i in range(len(lst)):
        if lst[i] > 1:
            tmp = lst[i]
            del lst[i]
            lst.insert(i, math.ceil(tmp/2))
            lst.insert(i, math.floor(tmp/2))
            if len(lst) == m:
                break

for x in lst:
    print(x, end=' ')

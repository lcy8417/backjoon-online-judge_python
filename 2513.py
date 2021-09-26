import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt", "r")

n, k, s = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(n)]
lt, rt = [], []
ans = 0


def calc(v):
    global ans
    pNum = 0
    tmp = 0
    while v:
        dis, cnt = heappop(v)
        tmp = max(-dis, tmp)
        if pNum + cnt > k:
            ans += tmp * 2
            heappush(v, (dis, cnt-(k-pNum)))
            pNum = 0
            tmp = 0
        else:
            pNum += cnt

    if tmp:
        ans += tmp * 2
        tmp, pNum = 0, 0


for x in info:
    if x[0] < s:
        heappush(lt, (x[0]-s, x[1]))
    if x[0] > s:
        heappush(rt, (s-x[0], x[1]))

calc(lt)
calc(rt)
print(ans)

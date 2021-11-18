import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

lt, rt = [], []
n = int(input())
for _ in range(n):
    x = int(input())
    if len(lt) == len(rt):
        heappush(lt, -x)
    else:
        heappush(rt, x)
    if rt and -lt[0] > rt[0]:
        l, r = -heappop(lt), heappop(rt)
        heappush(rt, l)
        heappush(lt, -r)
    print(-lt[0])

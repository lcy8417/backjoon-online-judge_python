import sys
from heapq import heappush, heappop, heapify
sys.stdin = open("input.txt", "r")

T = int(input())
while T:
    T -= 1
    n = int(input())
    f = list(map(int, input().split()))
    ans = 0
    heapify(f)
    while len(f) > 1:
        x, y = heappop(f), heappop(f)
        ans += x + y
        heappush(f, x+y)
    print(ans)

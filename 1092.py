import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
crein = list(map(int, input().split()))
m = int(input())
box = list(map(lambda x: int(x) * -1, input().split()))
heapq.heapify(box)
ch = [0 for _ in range(m)]
if max(crein) < max(box):
    print(-1)
else:
    crein.sort(reverse=True)
    ans = 0
    while len(box):
        for c in crein:
            for i in range(len(box)):
                if box[i] <= c:
                    del box[i]
                    break
        ans += 1
    print(ans)

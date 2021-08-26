import sys
import heapq
sys.stdin = open("input.txt", "r")

n, k = map(int, sys.stdin.readline().split())
heap = []
answer = 0
for _ in range(n):
    heapq.heappush(heap, list(map(int, sys.stdin.readline().split())))
bag = [int(sys.stdin.readline()) for _ in range(k)]
bag.sort()
tmp = []

for w in bag:
    while heap and heap[0][0] <= w:
        heapq.heappush(tmp, -heapq.heappop(heap)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not heap:
        break

print(answer)

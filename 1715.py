import sys
import heapq
# sys.stdin = open("input.txt", "r")

n = int(input())
heap = list(int(input()) for _ in range(n))
answer = 0
heapq.heapify(heap)
while heap:
    if len(heap) == 1:
        answer = 0
        break
    if len(heap) == 2:
        answer += heapq.heappop(heap) + heapq.heappop(heap)
        break
    x = heapq.heappop(heap) + heapq.heappop(heap)
    answer += x
    heapq.heappush(heap, x)
print(answer)

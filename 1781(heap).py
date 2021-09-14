import sys
import heapq
# sys.stdin = open("input.txt", "r")

n = int(input())
problem = [list(map(int, input().split())) for _ in range(n)]
problem.sort()

heap = []

for x in problem:
    heapq.heappush(heap, x[1])
    if x[0] < len(heap):
        heapq.heappop(heap)

print(sum(heap))

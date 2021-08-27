import sys
import heapq
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
study = [list(map(int, input().split())) for _ in range(n)]
study.sort()  # 일찍 시작하는 순

heap = []
for s, e in study:
    if not heap:
        heapq.heappush(heap, e)
    else:
        if heap[0] > s:
            heapq.heappush(heap, e)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, e)

print(len(heap))

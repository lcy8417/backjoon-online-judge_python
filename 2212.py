import sys
import heapq
sys.stdin = open("input.txt", "r")

n = int(input())
k = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
tmp = []
for i in range(len(arr)-1):
    heapq.heappush(tmp, -(arr[i+1]-arr[i]))

answer = -sum(tmp)
for _ in range(k-1):
    if tmp:
        answer += heapq.heappop(tmp)
    else:
        break

print(answer)

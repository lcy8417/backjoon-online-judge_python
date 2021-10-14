import sys
from collections import deque
sys.stdin = open("input.txt", "r")

s = int(input())
ch = [[0 for _ in range(2001)] for _ in range(2001)]
queue = deque()
queue.append([1, 0, 0])
while queue:
    bg, cl, time = queue.popleft()
    if bg == s:
        print(time)
        break
    if ch[bg][cl]:
        continue
    ch[bg][cl] = 1
    if bg >= 1:
        queue.append([bg-1, cl, time+1])
        queue.append([bg, bg, time+1])
    if cl and bg+cl <= 2000:
        queue.append([bg+cl, cl, time+1])

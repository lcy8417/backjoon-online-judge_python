import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

h, s, e, up, down = map(int, input().split())
ch = [0] * (h+1)
queue = deque()
queue.append([s, 0])
ch[s] = 1
while queue:
    x, cnt = queue.popleft()
    if x == e:
        print(cnt)
        sys.exit(0)
    lst = [x+up, x-down]
    for nx in lst:
        if 1 <= nx <= h and ch[nx] == 0:
            ch[nx] = 1
            queue.append([nx, cnt+1])

print('use the stairs')

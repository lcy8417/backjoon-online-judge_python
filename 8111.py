import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())

while T:
    T -= 1
    n = int(input())
    ch = [0 for _ in range(n)]
    queue = deque()
    answer = 'BRAK'
    queue.append([1 % n, '1'])
    while queue:
        x, tot = queue.popleft()
        if len(tot) > 100:
            break
        if x == 0:
            answer = int(tot)
            break
        t1, t2 = (x * 10 + 1) % n, (x * 10) % n
        if ch[t1] == 0:
            ch[t1] = 1
            queue.append([t1, tot+'1'])
        if ch[t2] == 0:
            ch[t2] = 1
            queue.append([t2, tot+'0'])
    print(answer)

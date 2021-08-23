import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())
prime = [0 for _ in range(10000)]
for i in range(2, 10000):
    if prime[i] == 0:
        for j in range(i+i, 10000, i):
            prime[j] = 1

while T:
    T -= 1
    n, m = map(int, input().split())
    answer = 'Impossible'
    ch = [0 for _ in range(10000)]
    queue = deque()
    queue.append([n, 0])
    ch[n] = 1
    while queue:
        x, cnt = queue.popleft()
        x1, x2, x3, x4 = x // 1000, (x % 1000) // 100, (x % 100) // 10, x % 10
        items = [x1, x2, x3, x4]
        if x == m:
            answer = cnt
            break
        for i in range(10):
            for j in range(4):
                t = items[j]
                items[j] = i
                tmp = items[0] * 1000 + items[1] * \
                    100 + items[2] * 10 + items[3]
                items[j] = t
                if 1000 <= tmp <= 9999 and ch[tmp] == 0 and prime[tmp] == 0:
                    ch[tmp] = 1
                    queue.append([tmp, cnt+1])
    print(answer)

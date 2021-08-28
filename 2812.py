import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))

answer = 0
stack = deque()

for i in range(n):
    while stack and k > 0:
        if stack[len(stack)-1] < num[i]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(num[i])

for i in range(len(stack)-k):
    print(stack[i], end='')

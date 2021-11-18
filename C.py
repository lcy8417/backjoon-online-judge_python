import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    n, m, d = map(int, input().split())
    field = [list(input()) for _ in range(n)]
    ch = [[0 for _ in range(m)] for _ in range(n)]
    ans = []
    queue = deque()
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        p = 1
        cnt = 0
        while True:
            if 0 <= x-p and 0 <= y-p and y+p < m and field[x-p][y-p] == '*' and field[x-p][y+p] == '*':
                cnt += 1
                p += 1
            else:
                break
        if cnt != 0:
            ans.append(cnt)
    print(ans)
    for i in range(1, d+1):
        if ans.count(i):
            print('NO')
            break
    else:
        print('YES')

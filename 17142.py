import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
birus = []
tmp = [[0, 0] for _ in range(m)]
answer = 2147000000
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def go(x, s):
    global answer
    if x == m:
        queue = deque()
        tmp_lab = [lab[i][:] for i in range(n)]
        maxx = 0
        flag = 0
        for xpos, ypos in tmp:
            queue.append([xpos, ypos, 0])
            tmp_lab[xpos][ypos] = 'o'
        while queue:
            cx, cy, dis = queue.popleft()
            if tmp_lab[cx][cy] != -1:
                maxx = max(dis, maxx)
            for k in range(4):
                nx, ny = cx+dx[k], cy+dy[k]
                if 0 <= nx < n and 0 <= ny < n and (tmp_lab[nx][ny] == '*' or tmp_lab[nx][ny] == 0):
                    if tmp_lab[nx][ny] == '*':
                        tmp_lab[nx][ny] = -1
                    elif tmp_lab[nx][ny] == 0:
                        tmp_lab[nx][ny] = dis+1
                    queue.append([nx, ny, dis+1])

        for i in range(n):
            for j in range(n):
                if tmp_lab[i][j] == 0:
                    flag = 1
                    break
            if flag:
                break

        if not flag:
            # if answer > maxx:
            #     for i in range(n):
            #         for j in range(n):
            #             print(tmp_lab[i][j], end=' ')
            #         print()
            #     print()
            answer = min(maxx, answer)

    else:
        for i in range(s, len(birus)):
            tmp[x] = birus[i]
            lab[birus[i][0]][birus[i][1]] = 0
            go(x+1, i+1)
            lab[birus[i][0]][birus[i][1]] = '*'


for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            birus.append([i, j])
            lab[i][j] = '*'
        elif lab[i][j] == 1:
            lab[i][j] = '-'

go(0, 0)
if answer == 2147000000:
    print(-1)
else:
    print(answer)

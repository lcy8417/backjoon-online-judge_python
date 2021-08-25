import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

n, m, d = map(int, input().split())
tower = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
archer = []
enemy = []
tmp = [[0, 0] for _ in range(3)]
answer = 0


def move_enemy(tmp, ch):
    cur_enemy = deque()
    while tmp:
        x, y = tmp.popleft()
        if x < n-1 and ch[x][y] == 0:
            cur_enemy.append([x+1, y])
    return cur_enemy


def go(x, s):
    global answer
    if x == 3:
        cnt = 0
        queue = deque(enemy)  # 현재 적들의 위치
        while queue:
            ch = [[0 for _ in range(m)] for _ in range(n)]
            for ax, ay in tmp:
                dis_lst = []
                for ex, ey in queue:
                    dis = abs(ex-ax) + abs(ey-ay)
                    if dis <= d:
                        dis_lst.append([ex, ey, dis])
                dis_lst.sort(key=lambda x: (x[2], x[1]))
                if len(dis_lst) and ch[dis_lst[0][0]][dis_lst[0][1]] == 0:
                    ch[dis_lst[0][0]][dis_lst[0][1]] = 1
                    cnt += 1
            queue = move_enemy(queue, ch)
        answer = max(answer, cnt)

    else:
        for i in range(s, m):
            tmp[x][0], tmp[x][1] = archer[i][0], archer[i][1]
            go(x+1, i+1)


for i in range(n):
    for j in range(m):
        if tower[i][j] == 1:
            enemy.append([i, j])

for i in range(m):
    archer.append([n, i])

go(0, 0)
print(answer)

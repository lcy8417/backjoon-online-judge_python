import sys
# sys.stdin = open("input.txt", "r")

h, n, w = map(int, input().split())
roop = [[0]*(w+1) for _ in range(h+1)]
answer = -1


def go(x):
    global answer, cnt
    if answer != -1:
        return
    if x == cnt:
        for index in range(1, h+1):  # 사다리 번호
            temp = index
            for p in range(1, w+1):
                nv = roop[temp][p]
                if nv:
                    temp += nv
            if temp != index:
                break
        else:
            answer = cnt
    else:
        for i in range(1, h):  # 사다리 번호
            for j in range(1, w+1):  # 깊이
                if roop[i][j] == 0 and roop[i+1][j] == 0:
                    roop[i][j] = 1
                    roop[i+1][j] = -1
                    go(x+1)
                    roop[i][j] = 0
                    roop[i+1][j] = 0


for _ in range(n):
    x, y = map(int, input().split())
    roop[y][x] = 1
    roop[y+1][x] = -1

for cnt in range(4):
    go(0)
    if answer != -1:
        break
print(answer)

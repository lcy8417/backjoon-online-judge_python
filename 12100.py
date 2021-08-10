import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def go(x, tmp):
    global answer
    if x == 5:
        for x in tmp:
            answer = max(answer, max(x))
    else:
        go(x+1, left(tmp))
        go(x+1, right(tmp))
        go(x+1, up(tmp))
        go(x+1, down(tmp))


def left(bd):
    tmp = [bd[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n-1):
            if tmp[i][j] == 0:
                for k in range(j+1, n):
                    if tmp[i][k]:
                        tmp[i][j], tmp[i][k] = tmp[i][k], tmp[i][j]
                        break
                else:  # 0이후 모든 숫자가 0 일때
                    break

            for k in range(j+1, n):
                if tmp[i][k]:
                    if tmp[i][k] == tmp[i][j]:
                        tmp[i][j] *= 2
                        tmp[i][k] = 0
                    break

    return tmp


def right(bd):
    tmp = [bd[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n-1, 0, -1):
            if tmp[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if tmp[i][k]:
                        tmp[i][j], tmp[i][k] = tmp[i][k], tmp[i][j]
                        break
                else:  # 0이후 모든 숫자가 0 일때
                    break

            for k in range(j-1, -1, -1):
                if tmp[i][k]:
                    if tmp[i][k] == tmp[i][j]:
                        tmp[i][j] *= 2
                        tmp[i][k] = 0
                    break

    return tmp


def up(bd):
    tmp = [bd[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n-1):
            if tmp[j][i] == 0:
                for k in range(j+1, n):
                    if tmp[k][i]:
                        tmp[j][i], tmp[k][i] = tmp[k][i], tmp[j][i]
                        break
                else:  # 0이후 모든 숫자가 0 일때
                    break

            for k in range(j+1, n):
                if tmp[k][i]:
                    if tmp[k][i] == tmp[j][i]:
                        tmp[j][i] *= 2
                        tmp[k][i] = 0
                    break

    return tmp


def down(bd):
    tmp = [bd[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n-1, 0, -1):
            if tmp[j][i] == 0:
                for k in range(j-1, -1, -1):
                    if tmp[k][i]:
                        tmp[j][i], tmp[k][i] = tmp[k][i], tmp[j][i]
                        break
                else:  # 0이후 모든 숫자가 0 일때
                    break

            for k in range(j-1, -1, -1):
                if tmp[k][i]:
                    if tmp[k][i] == tmp[j][i]:
                        tmp[j][i] *= 2
                        tmp[k][i] = 0
                    break

    return tmp


go(0, board)
print(answer)

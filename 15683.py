import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cctv = []
cnt = 0
answer = 2147000000


def watch(x, y, loc, tmp):
    croom = [tmp[i][:] for i in range(n)]
    cnt = 0
    for l in loc:
        if l == 'east':
            for i in range(y+1, m):
                if croom[x][i] == 6:
                    break
                if croom[x][i] == 0:
                    croom[x][i] = 9
                    cnt += 1
        elif l == 'west':
            for i in range(y-1, -1, -1):
                if croom[x][i] == 6:
                    break
                if croom[x][i] == 0:
                    croom[x][i] = 9
                    cnt += 1
        elif l == 'north':
            for i in range(x-1, -1, -1):
                if croom[i][y] == 6:
                    break
                if croom[i][y] == 0:
                    croom[i][y] = 9
                    cnt += 1
        elif l == 'south':
            for i in range(x+1, n):
                if croom[i][y] == 6:
                    break
                if croom[i][y] == 0:
                    croom[i][y] = 9
                    cnt += 1
    return croom, cnt


def go(x, sum, tmp):
    global answer
    if x == len(cctv):
        answer = min(answer, sum)
    else:
        xpos, ypos, kind = cctv[x]
        if kind == 1:
            cur, cnt = watch(xpos, ypos, ['east'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['south'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['west'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['north'], tmp)
            go(x+1, sum-cnt, cur)
        elif kind == 2:
            cur, cnt = watch(xpos, ypos, ['east', 'west'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['south', 'north'], tmp)
            go(x+1, sum-cnt, cur)
        elif kind == 3:
            cur, cnt = watch(xpos, ypos, ['north', 'east'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['east', 'south'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['south', 'west'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['west', 'north'], tmp)
            go(x+1, sum-cnt, cur)
        elif kind == 4:
            cur, cnt = watch(xpos, ypos, ['west', 'north', 'east'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['north', 'east', 'south'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['east', 'south', 'west'], tmp)
            go(x+1, sum-cnt, cur)
            cur, cnt = watch(xpos, ypos, ['south', 'west', 'north'], tmp)
            go(x+1, sum-cnt, cur)
        elif kind == 5:
            cur, cnt = watch(
                xpos, ypos, ['west', 'north', 'east', 'south'], tmp)
            go(x+1, sum-cnt, cur)


for i in range(n):
    for j in range(m):
        if room[i][j] == 0:
            cnt += 1
        elif room[i][j] != 6:
            cctv.append([i, j, room[i][j]])

go(0, cnt, room)
print(answer)

import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())


def cntGroup(x, y):
    lt, rt = 0, 0
    for i in range(n):
        if not(f[i][x] or f[i][j]):
            return False
        if f[i][x]:
            lt += 1
        if f[i][y]:
            rt += 1
    if min(lt, rt) < n // 2:
        return False
    return True


while T:
    T -= 1
    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    ans = 'NO'
    for i in range(4):
        for j in range(i+1, 5):
            if cntGroup(i, j):
                ans = 'YES'
                break
        if ans == 'YES':
            break
    print(ans)

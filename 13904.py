import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def go(x, sum, day, etc):
    global ans
    if ans >= sum + etc:
        return
    if x == n:
        ans = max(ans, sum)
    else:
        if work[x][0] >= day:
            go(x+1, sum+work[x][1], day+1, etc-work[x][1])
        go(x+1, sum, day, etc-work[x][1])


work.sort()
go(0, 0, 1, sum(work[i][1] for i in range(n)))
print(ans)

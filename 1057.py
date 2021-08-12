import sys
# sys.stdin = open("input.txt", "r")

n, s, e = map(int, input().split())
answer = -1
lst = [i for i in range(n)]


def go(x, f, a, b):
    global answer
    if answer != -1:
        return
    if a == b:
        answer = x
    if len(f) <= 1:
        return
    else:
        tmp = [i for i in range(int(len(f)/2+0.5))]
        go(x+1, tmp, a//2, b//2)


go(0, lst, s-1, e-1)
print(answer)

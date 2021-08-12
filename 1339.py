import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
lst = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
ch = [0] * 11
cnt = [0] * 26
alpha = []
answer = 0


def go(x):
    global answer
    if x == len(alpha):
        tot = 0
        for a in lst:
            tmp = 0
            for k in a:
                tmp = tmp*10 + cnt[k]
            tot += tmp
        answer = max(answer, tot)
    else:
        for i in range(10):
            if ch[i] == 0:
                ch[i] = 1
                cnt[alpha[x]] = i
                go(x+1)
                ch[i] = 0


for i in range(n):
    for j in range(len(lst[i])):
        if alpha.count(lst[i][j]) < 1:
            alpha.append(lst[i][j])

go(0)
print(answer)

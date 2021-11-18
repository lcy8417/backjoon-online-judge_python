import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())


def calc(lt, rt, ap):
    global cnt
    while lt < rt:
        if s[lt] == s[rt]:
            lt += 1
            rt -= 1
            continue
        if s[lt] == ap:
            lt += 1
            cnt += 1
        elif s[rt] == ap:
            rt -= 1
            cnt += 1
        else:
            return False
    return True


while T:
    T -= 1
    n = int(input())
    s = list(input())
    ans = 2147000000
    if calc(0, n-1, s):
        print(0)
        continue
    for i in range(26):
        ap = chr(97 + i)
        cnt = 0
        if calc(0, n-1, ap):
            ans = min(ans, cnt)
    print(ans if ans != 2147000000 else -1)

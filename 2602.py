import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

key = ['\0'] + list(input().strip())
eng = ['\0'] + list(input().strip())
dev = ['\0'] + list(input().strip())
dp = [[0 for _ in range(len(eng))] for _ in range(2)]
dp[0][0], dp[1][0] = 1, 1
ans = 0


def stone(a, p):
    global ans
    tmp = 0
    b = ''
    if a == dev:
        b = eng
    else:
        b = dev
    if a[j] == key[i]:
        for k in range(j-1, -1, -1):
            if b[k] == key[i-1]:
                tmp += dp[p][k]
        dp[not p][j] = tmp
        if i == len(key)-1:
            ans += tmp


for i in range(1, len(key)):
    for j in range(len(dev)-1, -1, -1):
        stone(eng, 1)
        stone(dev, 0)

print(ans)

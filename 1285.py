import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
coin = [list(input()) for _ in range(n)]
ans = 401


for bit in range(1 << n):
    new_coin = [coin[i][:] for i in range(n)]

    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if new_coin[i][j] == 'H':
                    new_coin[i][j] = 'T'
                else:
                    new_coin[i][j] = 'H'

    tot = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if new_coin[j][i] == 'T':
                cnt += 1
        tot += min(cnt, n-cnt)

    ans = min(ans, tot)

print(ans)

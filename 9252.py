import sys
# sys.stdin = open("input.txt", "r")

s1 = list(map(lambda x: ord(x), input()))
s2 = list(map(lambda x: ord(x), input()))
dp = [[0, ''] for _ in range(len(s2))]

for i in range(len(s1)):
    for j in range(len(s2)-1, -1, -1):
        if s1[i] == s2[j]:
            if dp[j][0] == 0:
                dp[j][0] = 1
                dp[j][1] = chr(s1[i])
            for k in range(j-1, -1, -1):
                if dp[k][0]+1 > dp[j][0]:
                    dp[j][0] = dp[k][0]+1
                    dp[j][1] = dp[k][1] + chr(s1[i])

dp.sort(key=lambda x: -x[0])
print(dp[0][0])
print(dp[0][1])

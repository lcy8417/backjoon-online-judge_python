import sys
# sys.stdin = open("input.txt", "r")

coin = [500, 100, 50, 10, 5, 1]
n = int(input())
balance = 1000 - n
answer = 2147000000
for i in range(6):
    tmp = balance
    cnt = balance // coin[i]
    tmp %= coin[i]
    for j in range(i+1, 6):
        cnt += tmp // coin[j]
        tmp %= coin[j]
        if tmp == 0:
            break
    answer = min(answer, cnt)

print(answer)

import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

dy = [0 for _ in range(21)]
dy[a[0]] = 1
for i in range(1, len(a)-1):
    tmp = [0 for _ in range(21)]
    x = a[i]
    for j in range(21):
        if x - j <= 0:
            tmp[j-x] += dy[j]
        if x + j <= 20:
            tmp[j+x] += dy[j]
    dy = tmp[:]

print(dy[a[n-1]])

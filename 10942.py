import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = [0] + list(map(int, sys.stdin.readline().split()))
m = int(input())
dy = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dy[i][i] = 1

for i in range(1, n):
    dy[i][i+1] = 1 if a[i+1] == a[i] else 0

for j in range(2, n):
    for i in range(n-j+1):
        k = j+i
        if dy[i+1][k-1] and a[i] == a[k]:
            dy[i][k] = 1
        else:
            dy[i][k] = 0

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dy[s][e])

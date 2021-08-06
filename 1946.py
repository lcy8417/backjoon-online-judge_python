import sys
sys.stdin = open("input.txt", "r")

T = int(input())
while T:
    n = int(input())
    cnt = n
    grade = [0 for _ in range(n+1)]
    for _ in range(n):
        i, x = map(int, input().split())
        grade[i] = x
    minn = grade[1]
    for i in range(2, n+1):
        if grade[i] > minn:
            cnt -= 1
        else:
            minn = grade[i]
    print(cnt)
    T -= 1

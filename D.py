import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


T = int(input())
while T:
    T -= 1
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        print(i, end=' ')
    print()

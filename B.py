import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    n = int(input())
    a = list(map(int, input().split()))
    print((2 ** a.count(0)) * a.count(1))

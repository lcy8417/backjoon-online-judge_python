import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    a, b, c = map(int, input().split())
    print((a*1 + b*2 + c*3) % 2)

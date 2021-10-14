import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1
    n = int(input())
    lst = list(map(int, input().split()))
    key = sum(lst) - sum(lst)*(n-2) / n
    lst.sort()
    ans = 0
    for i in range(n):
        for j in range(n-1, i, -1):
            if lst[i] + lst[j] > key:
                n = j
                break
            if lst[i] + lst[j] == key:
                ans += 1

    print(ans)

import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
tot = 0
for x in arr:
    if tot + 1 >= x:
        tot += x
    else:
        break
print(tot+1)

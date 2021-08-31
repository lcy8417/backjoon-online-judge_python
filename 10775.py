import sys
sys.setrecursionlimit(10**5)
# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ans = 0
imp = 0
airport = [0 for _ in range(n+1)]
find = [i for i in range(n+1)]
ex = [0 for _ in range(100000)]


def find_location(x):
    if x == 0:
        return -1
    if find[x] == x:
        find[x] -= 1
        return find[x]
    else:
        find[x] = find_location(find[x])
        return find[x]


for i in range(1, m+1):
    x = int(sys.stdin.readline())
    if imp:
        continue
    tmp = find_location(x)
    if tmp == -1:
        imp = 1
    else:
        ans += 1

print(ans)

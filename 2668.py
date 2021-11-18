import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
a = [0]
ans = [0, []]
ch = [0 for _ in range(n+1)]
for _ in range(n):
    a.append(int(input()))


def dfs(x, arr):
    global ans
    if x in arr:
        idx = arr.index(x)
        temp = arr[idx:]
        ans[1] += temp[:]
    else:
        if not ch[x]:
            ch[x] = 1
            dfs(a[x], arr[:] + [x])


for i in range(1, n+1):
    if not ch[i]:
        dfs(i, [])

ans[1].sort()
print(len(ans[1]))
for x in ans[1]:
    print(x)

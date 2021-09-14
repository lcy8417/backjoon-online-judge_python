import sys
# sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lt, rt = [0], [0]
ans = 0
for x in lst:
    if x < 0:
        lt.append(-x)
    else:
        rt.append(x)

lt.sort()
rt.sort()

for i in range(len(lt)-1, -1, -m):
    ans += lt[i] * 2

for i in range(len(rt)-1, -1, -m):
    ans += rt[i] * 2

if lt[len(lt)-1] > rt[len(rt)-1]:
    ans -= lt[len(lt)-1]
else:
    ans -= rt[len(rt)-1]
print(ans)

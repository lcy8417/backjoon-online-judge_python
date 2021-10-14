import sys
from math import factorial
sys.stdin = open("input.txt", "r")

n, m, k = map(int, input().split())
ans = ''


def getCombineCnt(x, y):
    return factorial(x+y) // (factorial(x) * factorial(y))


if getCombineCnt(m, n) < k:
    print(-1)
else:
    while True:
        if n == 0 or m == 0:
            break

        cnt = getCombineCnt(n-1, m)
        if cnt >= k:
            ans += 'a'
            n -= 1
        else:
            ans += 'z'
            m -= 1
            k -= cnt

    ans += 'z' * m + 'a' * n
print(ans)

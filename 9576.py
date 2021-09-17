import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def find(x):
    if x > b:
        return -1
    if x == unf[x]:
        unf[x] += 1
        return x
    else:
        tmp = find(unf[x])
        if tmp != -1:
            unf[x] = tmp
            return unf[x]
        else:
            return -1


while T:
    T -= 1
    ans = 0
    n, m = map(int, input().split())
    unf = [i for i in range(n+1)]
    scope = [list(map(int, input().split())) for _ in range(m)]
    scope.sort(key=lambda x: (x[1]))
    for a, b in scope:
        if find(a) != -1:
            ans += 1
    print(ans)

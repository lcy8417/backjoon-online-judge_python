import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def go(turn, x, y):
    if x == y:
        return card[x] if turn else 0
    if dp[x][y]:
        return dp[x][y]
    if turn:
        dp[x][y] = max(go(not turn, x+1, y) + card[x],
                       go(not turn, x, y-1) + card[y])
    else:
        dp[x][y] = min(go(not turn, x+1, y),
                       go(not turn, x, y-1))
    return dp[x][y]


T = int(input())
while T:
    T -= 1
    n = int(input())
    card = list(map(int, input().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    print(go(1, 0, n-1))

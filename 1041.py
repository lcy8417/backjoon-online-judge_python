import sys
sys.stdin = open("input.txt", "r")
INF = 250000000000001
answer = 0
n = int(input())
lst = list(map(int, input().split()))


def suffle():
    global dice
    dice[0] = min(lst)

    for i in range(6):
        for j in range(6):
            if i != j and i + j != 5:  # 반대편
                dice[1] = min(dice[1], lst[i] + lst[j])

    for i in [0, 5]:
        for j in [1, 4]:
            for k in [2, 3]:
                dice[2] = min(dice[2], lst[i] + lst[j] + lst[k])


dice = [INF for _ in range(3)]

if n == 1:
    lst.sort()
    print(sum(lst[:5]))
else:
    suffle()
    answer += 4 * (dice[2])  # 윗모서리
    answer += 4 * (dice[1])  # 아랫모서리
    if n > 2:
        answer += dice[0] * ((n-2) ** 2) * 5  # 중앙
        answer += dice[0] * (n-2) * 4  # 아랫측면
        answer += dice[1] * ((n-2) * 8)  # 나머지 측면

    print(answer)

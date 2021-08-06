import sys
# sys.stdin = open("input.txt", "r")

answer = []
minn = 2147000000
t = [300, 60, 10]
n = int(input())
for i in range(3):
    cnt = n // t[i]
    tmp = n % t[i]
    tmp_answer = [0 for _ in range(3)]
    tmp_answer[i] = cnt
    for j in range(i+1, 3):
        tmp_answer[j] = tmp // t[j]
        tmp %= t[j]
    if tmp == 0 and minn > cnt:
        minn = cnt
        answer = tmp_answer[:]

if len(answer) == 0:
    print(-1)
else:
    for x in answer:
        print(x, end=' ')

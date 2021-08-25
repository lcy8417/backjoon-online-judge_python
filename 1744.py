import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()
idx = 0
answer = 0
for i in range(n):
    if lst[i] >= 0:
        idx = i
        break
else:
    idx = n-1

for i in range(0, idx, 2):  # 0 까지
    if i+1 <= idx and lst[i+1] <= 0:
        answer += (lst[i] * lst[i+1])
    else:
        answer += lst[i]

for i in range(n-1, idx-1, -2):
    if i-1 >= idx:
        if lst[i] > 1 and lst[i-1] > 1:
            answer += (lst[i] * lst[i-1])
        else:
            answer += lst[i] + lst[i-1]
    else:
        answer += lst[i]

print(answer)

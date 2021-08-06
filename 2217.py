import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
answer = rope[0]
for i in range(len(rope)):
    answer = max(answer, rope[i] * (i+1))
print(answer)
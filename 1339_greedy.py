import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
pocket = [list(map(lambda x: ord(x)-65, input())) for _ in range(n)]
alpha = [0]*26
answer = 0

for word in pocket:
    tmp = 10 ** (len(word)-1)
    for c in word:
        alpha[c] += tmp
        tmp //= 10

alpha.sort(reverse=True)
order = 9
for x in alpha:
    answer += order * x
    order -= 1

print(answer)

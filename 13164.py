import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
kids = list(map(int, input().split()))
tmp = []
for i in range(1, len(kids)):
    tmp.append(kids[i]-kids[i-1])
tmp.sort(reverse=True)
print(sum(tmp[k-1:]))

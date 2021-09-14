import sys
# sys.stdin = open("input.txt", "r")

s = list(input())
t = list(input())

while len(t) != len(s):
    if t[len(t)-1] == 'A':
        t = t[:len(t)-1]
    else:
        t = list(reversed(t[:len(t)-1]))

if t == s:
    print(1)
else:
    print(0)

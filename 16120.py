import sys
# sys.stdin = open("input.txt", "r")

s = input()
tmp = 0
ans = 'PPAP'
if len(s) % 3 == 1:
    for i in range(len(s)):
        if s[i] == 'A':
            if i+1 < len(s) and tmp >= 2 and s[i+1] == 'P':
                tmp -= 2
            else:
                ans = 'NP'
                break
        else:
            tmp += 1
else:
    ans = 'NP'

if tmp != 1:
    ans = 'NP'
print(ans)

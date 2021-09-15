import sys
sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
lst = list(map(int, input().split()))
ch = [0 for _ in range(n+2)]
ans = 'YES'
room = [0]

for x in lst:
    room.sort(reverse=True)
    for i in range(len(room)):
        if room[i] < x:
            room[i] = x
            break
    else:
        room.append(x)
        if len(room) > k:
            ans = 'NO'
            break

print(ans)

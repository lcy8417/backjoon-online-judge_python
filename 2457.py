import sys
import heapq
# sys.stdin = open("input.txt", "r")

n = int(input())
flower = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(flower)):
    flower[i] = [flower[i][0]*100 + flower[i]
                 [1], flower[i][2]*100 + flower[i][3]]

ans = 0
cs, ce = 0, 0
spos, lpos = 0, 0
heap = []
flower.sort(key=lambda x: (x[0], x[1]))


while flower:
    s, e = flower.pop(0)
    s, e = max(301, s), min(e, 1201)
    if e < 301 or s >= 1201 or e <= s:
        continue
    if s == 301:
        spos = 301
    if s <= ce < e or (cs == 0 and ce == 0 and s == 301):
        heapq.heappush(heap, [-e, -s])
    elif s > ce or (cs == 0 and ce == 0 and s != 301):
        if not heap:
            ans = 0
            break
        x, y = heapq.heappop(heap)
        cs, ce = -y, -x
        lpos = ce
        ans += 1
        heap.clear()
        flower.insert(0, [s, e])

if heap and (spos != 301 or lpos < 1201):
    ans += 1
    lpos = -heapq.heappop(heap)[0]

if spos == 301 and lpos >= 1201:
    print(ans)
else:
    print(0)

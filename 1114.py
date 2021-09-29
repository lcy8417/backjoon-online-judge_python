import sys
sys.stdin = open("input.txt", "r")

INF = 1_000_000_001
l, k, c = map(int, input().split())
pos = [0] + list(map(int, input().split()))
pos.append(l)
pos.sort()
ans = [INF, INF]
dis = []


def cntCuting(x):
    tmp = 0
    cnt = 0
    idx = 0
    for i in range(k, -1, -1):
        if x < dis[i]:
            return -1, -1
        if x < tmp + dis[i]:
            tmp = dis[i]
            cnt += 1
            idx = i
            if cnt > c:
                return -1, -1
        else:
            tmp += dis[i]
    return cnt, idx


for i in range(1, len(pos)):
    dis.append(pos[i]-pos[i-1])

lt, rt = 0, l
while lt <= rt:
    mid = (lt + rt) // 2
    cnt, idx = cntCuting(mid)
    if cnt == -1:  # 불가능
        lt = mid + 1
    else:  # 가능
        rt = mid - 1
        ans[1] = mid
        if cnt < c:
            ans[0] = pos[1]
        else:
            ans[0] = pos[idx+1]

print(ans[1], ans[0])

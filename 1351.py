import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, p, q = map(int, input().split())
dic = {}
dic[0] = 1

def go(k):
    i, j = k // p, k // q
    if dic.get(k, 0):
        return dic[k]
    if not dic.get(i, 0):
        dic[i] = go(i)
    if not dic.get(j, 0):
        dic[j] = go(j)
    return dic[i] + dic[j]

print(go(n))

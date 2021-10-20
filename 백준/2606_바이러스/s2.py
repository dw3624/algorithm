import sys
sys.stdin = open('input.txt')


def dfs(s):
    for i in dic[s]:
        if i not in visit:
            visit.append(i)
            dfs(i)

def bfs(s):
    que = [s]
    while que:
        v = que.pop(0)
        for i in dic[v]:
            if i not in visit:
                visit.append(i)
                que.append(i)


n = int(input())
v = int(input())
dic = {}
for _ in range(v):
    s, e = map(int, input().split())
    dic.setdefault(s, []).append(e)
    dic.setdefault(e, []).append(s)
print(dic)

visit = []
dfs(1)
# bfs(1)

ans = len(visit)-1
print(ans)
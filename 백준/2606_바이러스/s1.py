def FindSet(x):
    if p[x] == x:
        return x
    else:
        return FindSet(p[x])
    # if p[x] != x:
    #     p[x] = FindSet(p[x])
    # return p[x]

def Union(x, y):
    x = FindSet(x)
    y = FindSet(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y


N = int(input())
p = list(range(N+1))

pair_num = int(input())
for _ in range(pair_num):
    x, y = map(int, input().split())
    Union(x, y)

ans = 0
for i in range(N+1):
    if FindSet(i) == 1:
        ans += 1
print(ans-1)
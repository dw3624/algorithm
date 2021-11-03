import sys
sys.stdin = open('input.txt')


def FindSet(x):
    # 부모노드가 자신이 아닌경우 재귀
    if P[x] != x:
        P[x] = FindSet(P[x])
    return P[x]


def Union(x, y):
    x = FindSet(x)  # x의 부모노드
    y = FindSet(y)  # y의 부모노드

    # 크기가 더 작은 부모노드로 갱신
    if x < y:
        P[y] = x
    else:
        P[x] = y


N, M = map(int, input().split())
P = list(range(N+1))

for _ in range(M):
    x, y = map(int, input().split())
    Union(x, y)

for i in range(len(P)):
    P[i] = FindSet(P[i])

ans = len(set(P))-1
print(ans)
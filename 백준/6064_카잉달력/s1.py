import sys
sys.stdin = open('input.txt')


def cal(m,n,x,y):
    k = x
    while k <= m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            return k
        k += m
    return -1


T = int(input())
for _ in range(T):
    M, N, X, Y = map(int, input().split())

    res = cal(M,N,X,Y)
    print(res)
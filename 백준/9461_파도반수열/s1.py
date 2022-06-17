import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    P = [0, 1, 1, 1]

    if N <= 3:
        print(P[N])
        continue
    for n in range(4, N+1):
        p = P[n-3] + P[n-2]
        P.append(p)

    print(P[N])
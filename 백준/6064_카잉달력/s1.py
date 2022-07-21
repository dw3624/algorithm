import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    k = x if x > y else y
    k_plus = M if x > y else N

    while k < M * N:
        if not (k-x)%M and not (k-y)%N:
            print(k)
            break
        k += k_plus
    else:
        print(-1)
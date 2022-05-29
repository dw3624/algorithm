import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    if not N % H:
        n1 = H
        n2 = N//H
    else:
        n1 = N % H
        n2 = N//H + 1

    ans = n1*100+n2
    print(ans)
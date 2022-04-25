import sys
sys.stdin = open('input.txt')

N, r, c = map(int, input().split())
ans = 0

while N > 0:
    # 전체 matrix를 4등분, 어느 사분면에 속하는지 확인
    N -= 1

    if r < 2**N and c < 2**N:
        ans += (4**N) * 0

    elif r < 2**N and c >= 2**N:
        ans += (4**N) * 1
        c -= 2**N

    elif r >= 2**N and c < 2**N:
        ans += (4**N) * 2
        r -= 2**N

    else:
        ans += (4**N) * 3
        r -= 2**N
        c -= 2**N

print(ans)

import sys
sys.stdin = open('input.txt')


import math


T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    k_max = math.floor(dist ** 0.5)

    if dist <= 3:
        cnt = dist
    elif dist**0.5 == k_max:
        cnt = k_max * 2 - 1
    elif k_max**2 < dist <= k_max**2+k_max:
        cnt = k_max * 2
    else:
        cnt = k_max * 2 + 1

    print(cnt)
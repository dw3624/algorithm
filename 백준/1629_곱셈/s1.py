import sys
sys.stdin = open('input.txt')

A, B, C = map(int, input().split())

# 모듈러 산술
# (a * b) % c = (a % c * b % c) % c
# 10^11 % 12 = (10^5 % 12 * 10^6 % 12) % 12
# 10^5 % 12 = (10^2 % 12 * 10^3 % 12) % 12
# ...
# 10^3 % 12 = (10^1 % 12 * 10^2 % 12) % 12

def func(k):
    if k == 1:
        return A % C

    num = func(k//2)

    if k % 2:
        return (num * num * A % C)%C
    else:
        return (num * num) % C


res = func(B)
print(res)


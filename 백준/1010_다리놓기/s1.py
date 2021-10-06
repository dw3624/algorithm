import sys
sys.stdin = open('input.txt')

def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    result = factorial(M) // (factorial(M-N) * factorial(N))
    print(result)

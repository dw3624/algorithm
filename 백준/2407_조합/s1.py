import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

def factorial(n, m = n):
    i = n
    num = 1
    while i > 1:
        if i == n - m:
            return num
        num *= i
        i -= 1
    return num

res = factorial(n, m) // factorial(m)
print(res)

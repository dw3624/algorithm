import sys
sys.stdin = open('input.txt')

zero = [1, 0]
one = [0, 1]

def fibonacci(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    fibonacci(N)

    print(zero[N], one[N])
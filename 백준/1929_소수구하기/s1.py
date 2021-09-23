import sys
sys.stdin = open('input.txt')


# n의 소수 여부 확인
def isprime(n):
    # n이 1인 경우 소수가 아니므로 False
    if n == 1:
        return False

    # n이 1이 아닌 경우
    else:
        # n이 n의 제곱근까지의 숫자들을 약수로 갖는지 확인
        for i in range(2, int(n**0.5)+1):
            # n이 나누어 떨어지는 경우 소수가 아니므로 False
            if n % i == 0:
                return False
        return True


M, N = map(int, input().split())

for num in range(M, N+1):
    if isprime(num):
        print(num)
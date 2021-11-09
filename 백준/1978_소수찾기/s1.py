import sys

sys.stdin = open('input.txt')


def isPrime(n):
    # 1 이하인 경우
    if n <= 1:
        return 0

    # 짝수인 경우 (2제외)
    elif not n % 2:
        return 1 if n == 2 else 0

    # 그외 숫자인 경우
    else:
        # 제곱근 숫자까지만 확인
        s_num = num ** 0.5
        # 3부터 2씩 더해가면 숫자 확인
        for i in range(3, int(s_num) + 1, 2):
            if not num % i:
                return 0
    return 1


N = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    cnt += isPrime(num)

print(cnt)
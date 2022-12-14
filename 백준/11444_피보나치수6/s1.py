import sys
sys.stdin = open('input.txt')

# 행렬 곱셈과 분할 정복을 사용해 피보나치 수를 구하는 문제입니다.
# DP로 풀 경우 시간와 메모리가 초과합니다.
# 피보나치 수열을 행렬로 바꿔 계산합니다. (참고: https://nukestorm.tistory.com/149)
# 분할 정복
#   []^k (k: 제곱수)
#   1) k = 1: 행렬 반환
#   2) k 홀수: []^k/2 * []^k/2 * []
#   3) k 짝수: []^k/2 * []^k/2



# 행렬의 곱셈
def multi(a, b):
    n = len(a)
    z = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            e = 0
            for i in range(n):
                e += a[r][i] * b[i][c]
            z[r][c] = e % p
    return z


# 분할 정복
def power(a, k):
    if k == 1:
        return a

    tmp = power(a, k//2)
    if k % 2:
        return multi(multi(tmp, tmp), a)
    else:
        return multi(tmp, tmp)


# 초기 행렬
fib_mat = [[1, 1], [1, 0]]
n = int(input())
p = 1000000007
print(power(fib_mat, n)[0][1])
import sys
sys.stdin = open('input.txt')


#10 20 10 30 20 50
#1  2  1  3  2  4
# 본인보다 작은 수 중 가장 큰 길이 + 1

N = int(input())
A = list(map(int, input().split()))
dp = [0] * N

for i in range(N):
    tmp_idx = i
    for j in range(i):
        if A[j] < A[i] and dp[tmp_idx] < dp[j]:
            tmp_idx = j
    dp[i] = dp[tmp_idx] + 1
    # print(dp)

print(max(dp))
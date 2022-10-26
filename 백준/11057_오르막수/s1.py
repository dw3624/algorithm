import sys
sys.stdin = open('input.txt')



# 2차원 dp
# row: 자릿수
# col: c(1~9)로 끝나는 숫자 개수
n = int(input())
nums = [[1] + [0] * 9 for _ in range(n - 1)]
nums = [[0] * 10] + [[1] * 10] + nums

for r in range(1, n+1):
    for c in range(1, 10):
        nums[r][c] = nums[r-1][c] + nums[r][c-1]
print(sum(nums[n]) % 10007)

import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
sum_nums = [[0]*(N+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, N+1):
        sum_nums[r][c] = sum_nums[r-1][c] + sum_nums[r][c-1] - sum_nums[r-1][c-1] + nums[r-1][c-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = sum_nums[x2][y2] - sum_nums[x2][y1-1] - sum_nums[x1-1][y2] + sum_nums[x1-1][y1-1]
    print(res)
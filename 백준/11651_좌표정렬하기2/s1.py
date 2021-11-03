import sys
sys.stdin = open('input.txt')

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
nums = sorted(nums, key=lambda x: [x[1], x[0]])
[print(*n) for n in nums]
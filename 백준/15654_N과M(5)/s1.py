import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print(nums)


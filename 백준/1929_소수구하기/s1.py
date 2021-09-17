import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
nums = list(range(M, N+1))
n = len(nums)


if nums[0] % 2:
    s = 1
else:
    s = 0

for i in range(s, n, 2):
    nums[i] = 0

for i, num in enumerate(nums):
    if num:
        for j in range(i + num, n, num):
            nums[j] = 0
    print(nums)

for num in nums:
    if num:
        print(num)
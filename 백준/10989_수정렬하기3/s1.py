import sys
sys.stdin = open('input.txt')


import sys

N = int(input())

nums = [0] * 10001
for _ in range(N):
    n = int(sys.stdin.readline())
    nums[n] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)
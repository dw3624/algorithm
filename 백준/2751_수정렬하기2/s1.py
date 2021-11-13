N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()

[print(num) for num in nums]
n, k = map(int, input().split())
nums = [input() for _ in range(n)]
nums.sort(key=lambda x: (len(x), x))
print(nums[k-1])

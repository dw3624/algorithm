import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = list(set((map(int, input().split()))))
nums.sort()

def func(idx, lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(idx, len(nums)):
        lst.append(nums[i])
        func(i, lst)
        lst.pop()
func(0, [])
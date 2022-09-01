import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def back(num, idx):
    if len(num) == M:
        print(*num)
        return
    for i in range(idx, N):
        num.append(nums[i])
        back(num, i)
        num.pop()

back([], 0)


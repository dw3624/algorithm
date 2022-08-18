# 시간초과
import sys
sys.stdin = open('input.txt')

N = int(input())

nums = [0]*10
nums[0], nums[-1] = [1], [8]
for n in range(1,9):
    nums[n] = [n-1, n+1]

def func(i, num, cnt):
    global res
    if cnt == N:
        # print(*num)
        return
    for n in nums[i]:
        # num.append(n)
        res += 1
        func(n, num, cnt+1)
        # num.pop()

res = 0
for i in range(1, 10):
    func(i, [i], 1)
print(res)
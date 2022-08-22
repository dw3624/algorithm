import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def back(lst, cnt):
    if cnt == M:
        print(*lst)
    for num in nums:
        if num not in lst:
            lst.append(num)
            back(lst, cnt+1)
            lst.pop()

back([], 0)
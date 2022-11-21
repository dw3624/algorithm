import sys
sys.stdin = open('input.txt')


from sys import stdin

nums = [True] * 1000001
for i in range(2, int(1000000**0.5) + 1):
    if nums[i]:
        for j in range(i + i, 1000001, i):
            nums[j] = False

while True:
    n = int(stdin.readline())
    if n == 0:
        break

    for k in range(2, n):
        if nums[k] and nums[n-k]:
            print(f'{n} = {k} + {n-k}')
            break

    else:
        print("Goldbach's conjecture is wrong.")
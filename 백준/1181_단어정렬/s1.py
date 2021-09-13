import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [input() for _ in range(N)]

lst = list(set(lst))
lst = sorted(lst, key=lambda x: (len(x), x))

for result in lst:
    print(result)


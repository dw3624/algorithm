import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        a, b = input().split()
        if clothes.get(b):
            clothes[b].append(a)
        else:
            clothes[b] = ['', a]

    res = 1
    for cloth in clothes:
        res *= len(clothes[cloth])
    print(res-1)
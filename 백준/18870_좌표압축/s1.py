import sys
sys.stdin = open('input.txt')


import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
num_set = sorted(set(lst))

dict = {}
for i in range(len(num_set)):
    dict[num_set[i]] = i

for l in lst:
    print(dict[l], end=' ')
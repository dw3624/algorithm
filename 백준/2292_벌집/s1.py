import sys
sys.stdin = open('input.txt')

N = int(input())
now = 1
layer = 0
while now < N:
    layer += 1
    now = now + 6*layer
print(layer+1)
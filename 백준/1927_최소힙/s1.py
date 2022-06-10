import sys
sys.stdin = open('input.txt')

def insert(x):
    heap.append(x)
    n = len(heap) - 1
    while n != 1 and x < heap[n]:
        heap[n], heap[n//2] = heap[n//2], heap[n]
        n //= 2

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x > 0:
        insert(x)
    if x == 0:
        if heap:
            print(heap.pop(0))
        else:
            print(0)
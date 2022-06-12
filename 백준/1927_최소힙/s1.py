import sys
sys.stdin = open('input.txt')

def insert(x):
    heap.append(x)
    n = len(heap)-1
    while n != 1 and x < heap[n]:
        heap[n], heap[n//2] = heap[n//2], heap[n]
        n //= 2

def delete(heap):
    heap[1], heap[-1] = heap[-1], heap[1]
    print(heap.pop())
    p = 1 # parent index
    while True:
        c = 2 * p # child index
        if c+1 < len(heap) and heap[c] > heap[c+1]:
            c += 1
        if c >= len(heap) or heap[c] > heap[p]: break

        heap[p], heap[c] = heap[c], heap[p]
        p = c


N = int(input())
heap = [0]

for _ in range(N):
    x = int(input())

    if x > 0:
        insert(x)
    if x == 0:
        if len(heap) > 1:
            delete(heap)
        else:
            print(0)
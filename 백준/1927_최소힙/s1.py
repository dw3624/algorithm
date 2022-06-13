import sys
sys.stdin = open('input.txt')


def insert(x):
    heap.append(x)
    n = len(heap)-1
    while n > 0 and heap[n] < heap[n//2]:
        heap[n], heap[n//2] = heap[n//2], heap[n]
        n //= 2


def delete(heap):
    if not heap:
        return print(0)

    heap[0], heap[-1] = heap[-1], heap[0]
    print(heap.pop())

    p = 0
    n = len(heap)
    while True:
        c = 2*p+1
        if c+1 < n and heap[c+1] < heap[c]:
            c += 1
        if c > n-1 or heap[p] < heap[c]:
            break
        heap[p], heap[c] = heap[c], heap[p]
        p = c


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x:
        insert(x)
    else:
        delete(heap)
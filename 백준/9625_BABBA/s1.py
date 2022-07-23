import sys
sys.stdin = open('input.txt')


K = int(input())
A = [1, 0]
B = [0, 1]

for k in range(2, K+1):
    a = A[k-1] + A[k-2]
    b = B[k-1] + B[k-2]
    A.append(a)
    B.append(b)
print(A[K], B[K])


import sys
sys.stdin = open('input.txt')

N = int(input())

num = 1
for n in range(2, N+1):
    num *= n

cnt = 0
while not num % 10:
    num //= 10
    cnt += 1

print(cnt)
import sys
sys.stdin = open('input.txt')


n = int(input())
N = 1
num = 666
while N < n:
    num += 1
    if '666' in str(num):
        N += 1
print(num)
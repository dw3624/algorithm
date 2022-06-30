import sys
sys.stdin = open('input.txt')

S = input()
T = input()
n = len(T)

while True:
    n -= 1
    if T[n] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

    if T == S:
        print(1)
        break
    elif not T:
        print(0)
        break
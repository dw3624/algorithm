import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    s = [0] * (11)
    s[1] = 1
    s[2] = 2
    s[3] = 4

    if n in [1,2,3]:
        print(s[n])
        continue

    for i in range(4, n+1):
        s[i] = s[i-1] + s[i-2] + s[i-3]
    print(s[n])
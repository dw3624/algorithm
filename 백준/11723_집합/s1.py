import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

M = int(input())
S = [0] * 21

for _ in range(M):
    cmd = input().rstrip()

    if 'add' in cmd:
        x = int(cmd.split()[1])
        S[x] = 1

    elif 'remove' in cmd:
        x = int(cmd.split()[1])
        S[x] = 0

    elif 'check' in cmd:
        x = int(cmd.split()[1])
        print(1) if S[x] else print(0)

    elif 'toggle' in cmd:
        x = int(cmd.split()[1])
        S[x] = 0 if S[x] else 1

    elif 'all' in cmd:
        S = [1] * 21

    else:
        S = [0] * 21
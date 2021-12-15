import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    cmd = input().rstrip()

    if 'add' in cmd:
        x = cmd.split()[1]
        S.add(int(x))

    elif 'remove' in cmd:
        x = cmd.split()[1]
        S.discard(int(x))

    elif 'check' in cmd:
        x = cmd.split()[1]
        print(1) if int(x) in S else print(0)

    elif 'toggle' in cmd:
        x = cmd.split()[1]
        x = int(x)
        S.discard(x) if x in S else S.add(x)

    elif 'all' in cmd:
        S = set(range(1, 21))

    else:
        S = set()
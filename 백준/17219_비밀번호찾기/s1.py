import sys
sys.stdin = open('input.txt')

import sys
N, M = map(int, sys.stdin.readline().split())
s = {}
for _ in range(N):
    id, pw = sys.stdin.readline().split()
    s[id] = pw

for _ in range(M):
    sid = sys.stdin.readline().strip()
    print(s[sid])
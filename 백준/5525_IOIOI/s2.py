import sys
sys.stdin = open('input.txt')

# 50점


N = int(input())
M = int(input())
S = input()
io = 'OI'*N
res = 0

for i in range(M):
    if S[i] == 'I':
        if S[i+1:i+1+len(io)] == io:
            # print(S[i:i+1+len(io)])
            res += 1

print(res)
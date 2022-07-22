import sys
sys.stdin = open('input.txt')

# 50점


N = int(input())
M = int(input())
S = input()
io = ['I', 'O']
# I에서 검사 시작
# IOIO 순서 확인
# N개 O 등장 후 종료

res = 0
for i in range(M):
    if S[i] == 'I':
        is_i = 1
        cnt = 0
        for j in range(i, M):
            if is_i and S[j] == 'I':
                cnt += 1
                is_i = 0
            elif not is_i and S[j] == 'O':
                is_i = 1
            else:
                break

            if cnt == N+1:
                res += 1
                break
print(res)
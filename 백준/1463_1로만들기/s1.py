import sys
sys.stdin = open('input.txt')

# N = 10
N = int(input())

cnts = [0]*(N+1)
for i in range(2, N+1):
    cnts[i] = cnts[i - 1] + 1

    if not i % 3:
        cnts[i] = min(cnts[i], cnts[i//3]+1)
    if not i % 2:
        cnts[i] = min(cnts[i], cnts[i//2]+1)

    # print(N, cnts)

print(cnts[N])

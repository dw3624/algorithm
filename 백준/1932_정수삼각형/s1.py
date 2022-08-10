import sys
sys.stdin = open('input.txt')


n = int(input())
stairs = [list(map(int, input().split())) for _ in range(n)]

k = 2
for i in range(1, n):
    for j in range(k):
        # 가장 첫 idx
        if j == 0:
            stairs[i][j] = stairs[i][j] + stairs[i-1][j]
        # 가장 뒤 idx
        elif j == i:
            stairs[i][j] = stairs[i][j] + stairs[i-1][j-1]
        # 중간 idx
        else:
            stairs[i][j] = stairs[i][j] + max(stairs[i-1][j-1], stairs[i-1][j])
    k += 1
print(max(stairs[-1]))
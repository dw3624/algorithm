import sys
sys.stdin = open('input.txt')

def chess(i, j, first_color):
    if first_color == 'W':
        colors = ['W', 'B']
    elif first_color == 'B':
        colors = ['B', 'W']

    cnt = 0
    for r in range(i, 8+i):
        for c in range(j, 8+j):
            tmp = colors[c % 2]
            if board[r][c] != tmp:
                cnt += 1
        colors.reverse()
    return cnt



N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

cnts = []
for row in range(N-8+1):
    for col in range(M-8+1):
        cnts.append(chess(row, col, 'W'))
        cnts.append(chess(row, col, 'B'))

result = sorted(cnts)[0]
print(result)
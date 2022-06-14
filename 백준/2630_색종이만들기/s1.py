import sys
sys.stdin = open('input.txt')


def sol(r, c, n):
    global blue, white

    # 하나라도 다른 색 나오는 경우 -> split
    color = paper[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != color:
                sol(r, c, n//2)
                sol(r+n//2, c, n//2)
                sol(r, c+n//2, n//2)
                sol(r+n//2, c+n//2, n//2)
                return

    # 모두 색 있는 경우
    if color:
        blue += 1
        return
    # 모두 색 없는 경우
    else:
        white += 1
        return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

sol(0, 0, N)

print(white)
print(blue)
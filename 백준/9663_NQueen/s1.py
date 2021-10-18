import sys
sys.stdin = open('input.txt')


def diagonal(r, c):
    """
    :param r: 현재 행
    :param c: 현재 열
    :return: 대각선 상에 있는 경우 False 반환
    """
    for i in range(r):
        # queen[i] : i번째 행에 놓인 퀸의 열 번호
        # (이전에 퀸이 놓인 행 번호) + (현재 행 번호 - 이전 행 번호) == 현재 열번호
        # (이전에 퀸이 놓인 행 번호) - (현재 행 번호 - 이전 행 번호) == 현재 열번호
        if queen[i] + (r - i) == c \
                or queen[i] - (r - i) == c:
            return False
    return True


def NQueen(r):
    """
    :param r: 현재 행
    """
    global queen, cnt

    if r == N:
        # print(queen)
        cnt += 1
        return

    for c in range(N):
        # 열 검사
        # 현재 열은 제외하고 퀸의 다음 자리를 탐색
        if not visit[c]:

            # 대각선 검사
            if diagonal(r, c):
                visit[c] = 1
                queen[r] = c

                NQueen(r+1)

                visit[c] = 0
                queen[r] = 0


N = int(input())

cnt = 0
visit = [0] * N   # 방문한 열 번호 저장
queen = [0] * N   # 퀸의 위치 (idx가 행번호, 각 idx 값이 열번호)
NQueen(0)

print(cnt)
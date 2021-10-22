import sys
sys.stdin = open('input.txt')


def func(sr, sc, n):
    # n x n 전체 그래프 탐색
    for r in range(sr, sr+n):
        for c in range(sc, sc+n):
            # 값이 하나라도 다르다면
            if mat[r][c] != mat[sr][sc]:
                n //= 3
                # 9개로 쪼갠 후 각각 탐색
                for nr in range(3):
                    for nc in range(3):
                        func(sr+(nr*n), sc+(nc*n), n)
                return

    # n x n 그래프 내부의 값이 모두 같다면 cnt 갱신신
    cnts[mt[sr][sc]+1] += 1


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
cnts = [0] * 3

func(0, 0, N)
[print(cnt) for cnt in cnts]
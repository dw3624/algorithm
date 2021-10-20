# import sys
# sys.stdin = open('input.txt')
# N, M, B = map(int, input().split())
# mat = [list(map(int, input().split())) for _ in range(N)]

import sys
N, M, B = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 초깃값 설정
time = float('inf')
height = 0

# 모든 높이에 대해 탐색 (내림차순)
for h in range(256, -1, -1):
    # up: 블럭 추가 횟수  down: 블럭 제거 횟수
    up = down = 0
    for r in range(N):
        for c in range(M):
            # 해당 블럭높이가 목표높이보다 낮을 경우
            if mat[r][c] < h:
                # 블럭 추가 횟수 +1
                up += h-mat[r][c]  # 사용해야할 보유블럭 수
            # 해당 블럭높이가 목표높이보다 높을 경우
            else:
                # 블럭 제거 횟수 +1
                down += mat[r][c]-h  # 보유블럭에 추가할 블럭 수

    # 보유 블럭이 부족한 경우
    # (총 보유블럭) < (사용블럭)
    if B+down < up:
        continue

    # 걸리는 총 시간
    tmp_time = down*2 + up*1

    # 걸리는 시간이 저장된 시간보다 짧을 경우 갱신
    # 걸리는 시간이 같은 경우 갱신 안함
    if tmp_time < time:
        time = tmp_time
        height = h

print(time, height)


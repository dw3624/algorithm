import sys
sys.stdin = open('input.txt')


from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(rr, rc, br, bc):
    que = deque()
    que.append((rr, rc, br, bc))
    visit = []
    visit.append((rr, rc, br, bc))
    cnt = 0

    while que:
        # que 길이만큼 for문으로 반복함으로써
        # 한번의 이동마다 cnt를 1씩 증가시킬 수 있다.
        for lq in range(len(que)):
            print(lq, 'cnt:', cnt, 'que:', que)
            rr, rc, br, bc = que.popleft()

            # cnt(이동횟수)가 10번 이상인 경우 -1
            if cnt > 10:
                print(-1)
                return

            # 빨간공이 출구에 도착한 경우 종료
            if mat[rr][rc] == 'O':
                print(cnt)
                return

            for d in range(4):
                nrr, nrc = rr, rc
                # 종료조건 걸릴때까지 반복시행
                while True:
                    nrr += dr[d]
                    nrc += dc[d]

                    # 벽에 부딪힌 경우 1칸 후퇴
                    if mat[nrr][nrc] == '#':
                        nrr -= dr[d]
                        nrc -= dc[d]
                        break
                    # 출구에 도착한 경우 반복문 종료
                    elif mat[nrr][nrc] == 'O':
                        break

                nbr, nbc = br, bc
                while True:
                    nbr += dr[d]
                    nbc += dc[d]

                    # 벽에 부딪힌 경우 1칸 후퇴
                    if mat[nbr][nbc] == '#':
                        nbr -= dr[d]
                        nbc -= dc[d]
                        break
                    # 출구에 도착한 경우 반복문 종료
                    elif mat[nbr][nbc] == 'O':
                        break

                # 파란공이 먼저 출구에 도착한 경우 다음 que로 skip
                if mat[nbr][nbc] == 'O':
                    continue

                # 빨간공과 파란공의 위치가 같을 때
                if nrr == nbr and nrc == nbc:
                    # 더 많이 이동한 공이 늦게 출발한 공이므로
                    # 해당 공은 1칸 후퇴
                    if abs(rr-nrr) + abs(rc-nrc) < abs(br-nbr) + abs(bc-nbc):
                        nbr -= dr[d]
                        nbc -= dc[d]
                    else:
                        nrr -= dr[d]
                        nrc -= dc[d]

                # 방문하지 않았다면 visit 추가
                if (nrr, nrc, nbr, nbc) not in visit:
                    que.append((nrr, nrc, nbr, nbc))
                    visit.append((nrr, nrc, nbr, nbc))
        # 이동횟수 갱신
        cnt += 1
    # que를 다 돌았는데 도착점에 도착하지 못한 경우 -1
    print(-1)


N, M = map(int, input().split())
mat = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if mat[r][c] == 'R':
            rr, rc = r, c
        elif mat[r][c] == 'B':
            br, bc = r, c

bfs(rr, rc, br, bc)
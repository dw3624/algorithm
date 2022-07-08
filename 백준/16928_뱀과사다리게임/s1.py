import sys
sys.stdin = open('input.txt')


from collections import defaultdict

N, M = map(int, input().split())
shortcut = defaultdict(int)
for _ in range(N+M):
    x, y = map(int, input().split())
    shortcut[x] = y

# 주사위 6만 나왔을때 100번 칸 도착까지 굴려야하는 횟수
res = 100//6
def bfs():
    global res
    visit = [1e9]*101
    q = [(1, 0)]

    while q:
        num, cnt = q.pop(0)
        # print(num, cnt, q)

        # 굴린횟수가 답보다 작은 경우 탐색 중단
        if cnt > res:
            continue
        # 94보다 큰 값 나온 경우 탐색 중단 및 답 갱신
        if num >= 94:
            res = min(res, cnt)
            continue

        for i in range(6, 0, -1):
            if shortcut[num+i] > 0:
                next_num = shortcut[num+i]
            else:
                next_num = num+i

            # 방문한 숫자 칸에 기록된 굴린 횟수보다 작을 경우 q에 추가
            if visit[next_num] > cnt+1:
                visit[next_num] = cnt+1
                q.append((next_num, cnt+1))

bfs()
print(res+1)

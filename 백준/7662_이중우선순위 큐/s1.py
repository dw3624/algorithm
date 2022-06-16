import sys
sys.stdin = open('input.txt')

import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    visit = [False]*K
    Q1 = []     # 최소힙
    Q2 = []     # 최대힙

    for k in range(K):
        x, n = sys.stdin.readline().split()
        n = int(n)

        if x == 'I':
            visit[k] =True
            heapq.heappush(Q1, (n, k))
            heapq.heappush(Q2, (-n, k))

        else:
            if n==-1:
                while Q1 and not visit[Q1[0][1]]:
                    heapq.heappop(Q1)
                if Q1:
                    visit[Q1[0][1]] = False
                    heapq.heappop(Q1)

            elif n==1:
                while Q2 and not visit[Q2[0][1]]:
                    heapq.heappop(Q2)
                if Q2:
                    visit[Q2[0][1]] = False
                    heapq.heappop(Q2)

    while Q1 and not visit[Q1[0][1]]:
        heapq.heappop(Q1)
    while Q2 and not visit[Q2[0][1]]:
        heapq.heappop(Q2)

    if not Q1 and not Q2:
        print('EMPTY')
    else:
        print(-Q2[0][0], Q1[0][0])
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(2):
    N, M = map(int, input().split())
    docs = [int(x) for x in input().split()]
    que = [[i, doc] for i, doc in enumerate(docs)]

    v_set = que.pop(0)
    while que:
        v = v_set[1]

        if v < max(docs):
            que.append(v_set)

        else:
            v_set = que.pop(0)








    # 현재 문서 중요도 검사
    # 나머지 문서 중요도 비교
    # pop이면 해당 문서 중요도 0으로
    # M번째 문서 중요도 0인 경우 종료
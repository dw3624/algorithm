import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    docs = [int(x) for x in input().split()]
    que = [[i, doc] for i, doc in enumerate(docs)]


    cnt = 0
    while que:
        v = que.pop(0)

        if v[1] < max(docs):
            que.append(v)
            # print(que)

        else:
            docs[v[0]] = 0
            cnt += 1
            # print('cnt up to', cnt)

            if docs[M] == 0:
                print(cnt)
                break




import sys
sys.stdin = open('input.txt')


# dfs를 사용해 해결할 수 있는 문제입니다.
# dfs 정의
# 표시할 수열을 인자로
# 수열 길이 M일 때 return 및 출력
# 입력된 수열 순회
# 방문하지 않았고 다른 값인 경우 push
# - 입력 수열이 1,7,9,9과 같이 같은 숫자가 여러개일 경우 중복된 수열 생성
# - remember 변수 따로 생성해 이전에 추가한 숫자와 같은지 검사


N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
visit = [0] * N


def dfs(nums):
    if len(nums) == M:
        print(*nums)
        return

    remember = 0
    for i in range(N):
        if not visit[i] and remember != num_lst[i]:
            visit[i] = 1
            nums.append(num_lst[i])
            remember = num_lst[i]
            dfs(nums)
            visit[i] = 0
            nums.pop()
    return

dfs([])
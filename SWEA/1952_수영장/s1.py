import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    day, a_mon, thr_mon, year = map(int, input().split())
    plans = [0] + list(map(int, input().split()))
    fee = [0]

    for i in range(1, len(plans)):
        swim = plans[i]  # 수영장 이용횟수

        fee1 = fee[i-1] + swim*day  # 1일 이용권 사용했을 때 비용
        fee2 = fee[i-1] + a_mon     # 1달 이용권 사용했을 때 비용

        if i < 3:
            fee3 = thr_mon
        else:
            fee3 = fee[i-3] + thr_mon

        tmp = sorted([fee1, fee2, fee3])
        fee.append(tmp[0])

    # 1년 이용권 비용과 비교
    if fee[-1] < year:
        answer = fee[-1]
    else:
        answer = year

    print('#{} {}'.format(tc, answer))




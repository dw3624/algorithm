import sys
sys.stdin = open('input.txt')


# 암호 사전 생성
pw = {'0001101': '0',
      '0011001': '1',
      '0010011': '2',
      '0111101': '3',
      '0100011': '4',
      '0110001': '5',
      '0101111': '6',
      '0111011': '7',
      '0110111': '8',
      '0001011': '9',}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # dummy row 제거, 검증코드 추출
    orig_nums = ''
    cert_code = 0
    for _ in range(N):
        tmp_line = input()
        if '1' in tmp_line:
            orig_nums = tmp_line
            cert_code += 1


    # 56자리 고유번호 추출
    i = M-1
    while orig_nums[i] == '0':
        i -= 1
    nums = orig_nums[i-56+1:i+1]


    # 7자리 분할
    num_lst = []
    for j in range(0, 56, 7):
        num_lst.append(nums[j:j+7])


    # 상품코드 변환
    product_num = []
    for n in num_lst:
        if pw.get(n):
            product_num.append(int(pw[n]))

    # 각 상품코드 계산
    tmp1, tmp2 = 0, 0
    for p in range(8):
        if p % 2:
            tmp1 += product_num[p]
        else:
            tmp2 += product_num[p]
    tmp_sum = tmp1 + (tmp2*3)


    # 10의 배수 여부 확인, 정답 출력
    if tmp_sum % 10:
        answer = 0
    else:
        answer = sum(product_num)
    print('#{} {}'.format(tc, answer))
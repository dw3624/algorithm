import sys
sys.stdin = open('input.txt')

# 중위 표기식을 후위 표기식으로 바꾸는 문제입니다.
# 연산자 우선순위에 맞춰 stack과 결과값에 문자를 저장합니다.
# 1. 연산자를 저장할 stack, 결과값 저장할 res 변수 생성
# 2. 수식 문자 순환
#   1) `(`: stack 추가
#   2) `*`,`/`: 이어진 곱셈 나눗셈 연산자 pop, res에 추가
#   3) `+`,`-`: `(`가 나올 때까지 pop, res에 추가
#   4) `)`: `(`가 나올 때까지 pop, `(`도 pop
#   5) 기타 문자: res에 추가


text = input()
stack = []
res = ''

for t in text:
    if t == '(':
        stack.append(t)
    elif t in ['*', '/']:
        while stack and (stack[-1] in ['*', '/']):
            res += stack.pop()
        stack.append(t)
    elif t in ['+', '-']:
        while stack and (stack[-1] != '('):
            res += stack.pop()
        stack.append(t)
    elif t == ')':
        while stack and (stack[-1] != '('):
            res += stack.pop()
        stack.pop()
    else:
        res += t

while stack:
    res += stack.pop()
print(res)

import sys
sys.stdin = open('input.txt')


N = int(input())
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()
ans = abs(100-N) ## +/- 만을 이용하는 경우 (최대횟수)

for num in range(500000*2+1):
    for n in str(num):
        if n in broken:
            break
    else:
        # min(기존답, 번호 누른 횟수 + +/- 누르는 횟수)
        ans = min(ans, len(str(num))+abs(num-N))

print(ans)
import sys
sys.stdin = open('input.txt')


while nums True:
    nums = input()
    if nums == '0':
        break
    elif nums == nums[::-1]:
        print('yes')
    else:
        print('no')
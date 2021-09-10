import sys
sys.stdin = open('input.txt')

x, y, w, h = map(int, input().split())

distances = [x-0, y-0, w-x, h-y]

print(min(distances))

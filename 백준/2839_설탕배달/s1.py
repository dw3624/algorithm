import sys
sys.stdin = open('input.txt')

sugar = int(input())
bag = 0

while sugar >= 0:
    if not sugar % 5:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1

else:
    print(-1)
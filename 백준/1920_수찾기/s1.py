import sys
sys.stdin = open('input.txt')


def binary(n):
    left = 0
    right = len(nums1) - 1
    while left <= right:
        mid = (left + right) // 2
        # print(n, left, right, mid, nums1[mid])
        # print()

        if n < nums1[mid]:
            right = mid - 1

        elif n > nums1[mid]:
            left = mid + 1

        elif n == nums1[mid]:
            return 1
    return 0


N = int(input())
nums1 = list(map(int, input().split()))
nums1.sort()
M = int(input())
nums2 = list(map(int, input().split()))

for num2 in nums2:
    print(binary(num2))









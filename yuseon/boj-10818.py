# 파이썬 스타일 풀이
N = int(input())
nums = list(map(int,input().split()))
print(min(nums), end=" ")
print(max(nums))

"""
# C 스타일 풀이
import sys

N = int(input())
nums = list(map(int,input().split()))
max = -sys.maxsize
min = sys.maxsize
for n in nums:
    if n > max:
        max = n
    elif n < min:
        min = n
    else:
        continue
print(min, end=" ")
print(max)
"""
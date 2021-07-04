import sys

nums = list(map(int, sys.stdin.readline().split()))

A = nums[0]
B = nums[1]
C = nums[2]

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print((A%C)*(B%C)%C)


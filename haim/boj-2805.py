import sys

tree_num, tree_len = map(int, sys.stdin.readline().split(' '))

trees = sys.stdin.readline().split()
trees = list(map(int, trees))

start, end = 1, max(trees)

while start <= end:
    mid_len = (start + end) // 2
    sum_len = 0

    for i in trees:
        if mid_len <= i:
            sum_len += (i - mid_len)

    if sum_len >= tree_len:
        start = mid_len + 1
    else:
        end = mid_len - 1

print(end)

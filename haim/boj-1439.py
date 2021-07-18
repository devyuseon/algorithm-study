import sys

arr = sys.stdin.readline()

len_arr = len(arr)

cnt = 0

for i in range(1, len(arr)-1):
    current = arr[i-1]
    if current != arr[i]:
        cnt += 1

print(cnt//2 if cnt % 2 == 0 else cnt // 2 + 1)
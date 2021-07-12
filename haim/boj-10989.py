# 시간 제한과 메모리 제한으로 배열을 선언하는 순간 메모리가 오버됨
# 블로그 참고
# 입력되는 숫자의 제한이 10000이라는 것이 조건이므로
# 10000 크기의 배열을 만들어서 해당하는 (0 - 9999 이므로 1이들어올경우 0번째에 저장)
# 배열의 위치의 값을 +1 시킴으로 갯수를 측정.
# 이후에는 (배열의 위치 + 1)의 값을 for문으로 돌면서 갯수만큼 출력하면 정렬이 된 것같은 결과가 나옴.


import sys

n = int(sys.stdin.readline())

'''
from sys import stdin

sr = lambda : stdin.readline()
n = int(sr())

원본 코드에서는 이렇게 써있던데 왜그런거지
'''

arr = [0 for _ in range(10000)]

for _ in range(n):      # 입력받은 숫자와 같은 arr의 값을 +1
    arr[int(sys.stdin.readline()) - 1] += 1

for i in range(len(arr)):       # 배열을 순서대로 접근해서 출력
    if arr[i] != 0:
        for j in range(arr[i]):     # 0이 아닌 만큼 반복해서 출력
            print(i + 1)        # 실제 값에 맞춰서 + 1
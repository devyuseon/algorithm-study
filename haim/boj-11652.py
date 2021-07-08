# collections 모듈 사용
# https://bnzn2426.tistory.com/95 참고 블로그

import collections
import sys


n = int(input())
arr = []
result = []

while n > 0:
    n -= 1

    input_arr = sys.stdin.readline().rstrip()
    arr.append(int(input_arr))       # 입력받은 숫자를 list 저장

cnt = collections.Counter(arr)      # arr의 원소의 빈도를 cnt에 dict 형식으로 저장함
# ex) Counter({'1': 3, '2': 2})
max_value = max(list(cnt.values()))     # dict 값에서 가장 큰 value값을 저장
for key in list(cnt.keys()):        # dict 형식의 cnt에서 key값을 가져와서
    if cnt[key] == max_value:       # key값을 통해서 value를 가져오고 max값과 비교
        result.append(key)      # 비교한 값이 같다면 해당 key값들을 결과 출력용 list에 저장

# 이 때 result에는 value 값이 같은 key들이 들어오게된다. (하나가 아닐 수도 있다는 것)
# 최대 값이 여러개일 경우는 가장 작은 값을 출력하라고 했기 때문에 정렬해야함.
# 값이 하나인 경우는 어차피 무슨 sort든 예외상황으로해서 그냥 바로 출력되게 하면 됨
# 정렬은 삽입정렬이 가장 괜찮을 듯.

print(min(result))

# insertion 정렬로 했는데 시간초과남. 애초에 정렬 문제가 아닌듯하다.

# if len(result) == 1:
#     print(result[0])
#
# else:
#     for i in range(1, len(result)):
#         for j in range(i, 0, -1):
#             if result[j] < result[j-1]:
#                 temp = result[j]
#                 result[j] = result[j-1]
#                 result[j-1] = temp
#     print(result[0])

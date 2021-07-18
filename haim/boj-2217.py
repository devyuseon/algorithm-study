import sys


n = int(input())

rope_arr = [sys.stdin.readline().strip("\n") for _ in range(n)]
rope_arr = list(map(int, rope_arr))


# 모든 로프를 이용하지 않아도 되기 때문에 최소값을 찾는게 아니라
# 로프별로 전체 중량을 나눠들었을 때 최대값이 나오는 로프를 찾아야함
# 1 4 5 6 7로 예를 들면 4,5,6,7 로프를 선택했을 때 최대값이므로 4*4=16이 최대값
# 1. 정렬해야함
# 2. 정렬된 상태에서 순서대로 배열 요소값이랑 배열길이 len (-1)줄여가면서 max 찾아야함
# 3. 찾은 max값일 때의 최소값인 요소값을 min에, 그 때의 남은 요소들(len)을 저장
# 4. 결과는 min * len

rope_arr_sorted = sorted(rope_arr)

rope_len = len(rope_arr)
Max = 0
Min = 10000

while rope_len > 0:
    for i in rope_arr_sorted:
        if i * rope_len > Max:
            Max = i * rope_len
            Min = i
            seleted_ropes = rope_len
        rope_len -= 1

print(Min * seleted_ropes)
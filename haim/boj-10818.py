n = int(input(""))      # 입력받을 문자 수
arr = list(map(int, input().split()))       #입력받은 값을 공백으로 구분(split)해서 int변환(map), 리스트로 변환(list)

cnt = 0     #처음 들어오는 값 거르기
for i in arr:
    if (cnt == 0):
        min = i
        max = i
    else:
        if(i < min):
            min = i
        if(i > max):
            max = i
    cnt += 1

print(min, max)



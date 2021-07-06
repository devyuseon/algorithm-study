n = int(input(""))      # 입력받을 문자 수
arr = list(map(int, input().split()))       #입력받은 값을 공백으로 구분(split)해서 int변환(map), 리스트로 변환(list)
print(min(arr), max(arr))



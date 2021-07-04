import sys

n = int(input())

while n != 0:
    n -= 1
    str1 = []       # 문자열 앞에 절반
    str2 = []       # 문자열 뒤에 절반(대칭)

    inputStr = sys.stdin.readline().strip("\n")     # strip이 공백을 없애는 상태로 설정되어있어서 공백이있는 문자열의 경우 에러발생. "\n"으로 수정

    for i in range(0, len(inputStr)//2):     # 앞에 절반 대문자 확인하고->그냥 전부 소문자로 출력시켜버리면? str1
        if inputStr[i].isupper():
            str1.append(inputStr[i].lower())
        else:
            str1.append(inputStr[i])
    for i in range(len(inputStr) - 1, len(inputStr)//2 + (len(inputStr) % 2 - 1), -1):   # 글자길이 짝/홀 에 따라서 절반 자르기
        if inputStr[i].isupper():
            str2.append(inputStr[i].lower())
        else:
            str2.append(inputStr[i])

    if str1 == str2:     # str1,2 같은지 확인해서 펠린드롬 반환
        print("Yes")
    else:
        print("No")

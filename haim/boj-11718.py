import sys

arr =[]

while True:
    n = input("")
    arr.append(n)
    if n == '':
        break

for i in range(0,len(arr)-1,1):
    print(arr[i])
        #아니 EOFerror라는데 아마 arr끝에 뭔가 잘못돼서 그렇겠지..


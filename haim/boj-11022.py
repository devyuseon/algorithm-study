arr = []
n = int(input())

for i in range(0, n):
    num1, num2 = map(int, input().split())
    plus = num1 + num2
    result = ("Case #"+str(i+1)+":"+" "+str(num1)+" "+"+"+" "+ str(num2)+" "+"="+" "+ str(plus))
    arr.append(result)

for cnt in range(0, len(arr)):
    print(arr[cnt])



def printStar(num):
    for i in range(1, num + 1, 1):
        print("*" * (num - i + 1))

n = int(input(""))
printStar(n)


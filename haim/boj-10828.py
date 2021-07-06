import sys

n = int(input())
stack =[]


while(n > 0):

    n -= 1
    order = sys.stdin.readline().split()

    if 'pop' == order[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
            stack.pop(0)
    elif 'size' == order[0]:
        print(len(stack))
    elif 'empty' == order[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' == order[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    else:       # push 연산
        num = int(order[1])
        stack.insert(0,num)
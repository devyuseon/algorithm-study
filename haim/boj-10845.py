import sys

n = int(input())
queue =[]


while(n > 0):
    n -= 1
    order = sys.stdin.readline().split()

    if 'pop' == order[0]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif 'size' == order[0]:
        print(len(queue))
    elif 'empty' == order[0]:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' == order[0]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' == order[0]:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
    else:       # push 연산
        num = int(order[1])
        queue.append(num)
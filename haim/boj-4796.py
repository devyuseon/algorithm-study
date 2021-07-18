import sys

num = 0
while True:
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break
    num += 1
    result = V//P*L + (L if V % P > L else V % P)

    print(f"Case {num}: {result}")

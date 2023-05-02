import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    line = input().strip()
    flag = True

    for i in line:
        if i == "(":
            stack.append(1)
        elif i == ")":
            if len(stack) == 0:
                print("NO")
                flag = False
                break
            else:
                stack.pop()
    if flag:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")

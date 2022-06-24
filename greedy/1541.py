import sys

input = sys.stdin.readline

str = list(input())
arr = []

num = ""

for s in str:
    if s == "+" or s == "-":
        if num != "":
            arr.append(int(num))
            num = ""
        arr.append(s)
    else:
        num += s

if num != "":
    arr.append(int(num))

flag = False
minus = 0
result = 0

for a in arr:
    if a == "+":
        continue
    elif a == "-":
        result -= minus
        minus = 0
        flag = True
    elif flag == True:
        minus += a
    else:
        result += a

if minus:
    result -= minus

print(result)

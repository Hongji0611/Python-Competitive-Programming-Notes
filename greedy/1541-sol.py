from array import array
import sys

input = sys.stdin.readline

arr = input().split('-')

list = []

for a in arr:
    plus = a.split('+')
    sum = 0
    for p in plus:
        sum += int(p)
    list.append(sum)

result = list[0]

for i in range(1, len(list)):
    result -= list[i]

print(result)

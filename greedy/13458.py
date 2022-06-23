import sys

input  = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0

for i in range(n):
    list[i] = list[i] - b
    result += 1

    if list[i] > 0:
        result += list[i] // c
        if list[i] % c != 0:
            result += 1

print(result)

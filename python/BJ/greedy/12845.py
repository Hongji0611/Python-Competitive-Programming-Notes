import sys

#레벨은 크기가 큰 순서로 입력된다.

input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))

list.sort()
result = 0

for i in range(0, n-1):
    result += list[i]

result += (n-1) * list[n-1]

print(result)
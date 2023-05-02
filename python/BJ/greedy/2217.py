import sys

input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort()

result = 0

for i in range(0, n):
    now = list[i] * (n-i) # 가장 작은 무게 * 나머지 개수
    if now > result:
        result = now

print(result)

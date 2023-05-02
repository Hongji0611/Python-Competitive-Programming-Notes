import heapq
import sys

input = sys.stdin.readline
n = int(input())

list = []
for i in range(n):
    s, t = map(int, input().split())
    list.append([s, t])

list.sort(key=lambda x: x[0])

result = []
heapq.heappush(result, list[0][1])

for i in range(1, n):
    if result[0] > list[i][0]:
        heapq.heappush(result, list[i][1])
    else:
        heapq.heappop(result)
        heapq.heappush(result, list[i][1])

print(len(result))

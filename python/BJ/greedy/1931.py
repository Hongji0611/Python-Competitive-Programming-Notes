import sys

input = sys.stdin.readline

n = int(input())

list = []

for i in range(n):
    s, f = map(int, input().split())
    list.append([s, f])

list.sort(key= lambda x: (x[1], x[0])) #빨리 끝나는 순, 빨리 시작하는 순

print(list)

end_time = 0
count = 0

for i in range(n):
    if end_time <= list[i][0]: # 시작 시간과 끝나는 시간이 같을 때도 고려
        end_time = list[i][1]
        count += 1

print(count)

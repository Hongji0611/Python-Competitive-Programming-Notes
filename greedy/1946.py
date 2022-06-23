import sys

input = sys.stdin.readline

#지원자의 숫자가 100,000이므로 n log n 만에 수행해야 함. (이중 for문 불가)
#서류, 면접 순위 중 서류를 기준으로 오름차순 정렬을 하면
#면접 순위는 본인의 앞 사람을 기준으로 숫자가 작으면 채틱된다.
#즉, 앞사람들 중 가장 숫자가 작은 것을 기준으로 이 숫자보다 작은 경우 채택된다. 

t = int(input())
for _ in range(t):
    n = int(input())
    list = []
    result = 0
    for _ in range(n):
        a, b = map(int, input().split())
        list.append([a, b])
    list.sort(key = lambda x: x[0])
    
    min = n+1
    for user in list:
        if user[1] < min:
            result += 1
            min = user[1]

    print(result)

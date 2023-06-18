# 풀이1: 모든 수를 나누어서 계산
# 풀이2: 소수는 제곱근까지만 계산
# 풀이3: 에라토스테네스의 체


import math

def solution(n):
    answer = 0

    for i in range(2, n+1):
        flag = False
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0 and j != i:
                flag = True
                break
        if flag == False:
            answer += 1

    return answer

def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(2*i, n+1, i)

    return len(num)

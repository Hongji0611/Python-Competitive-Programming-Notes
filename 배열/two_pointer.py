# 부분연속의 합이 n을 만족하는 방법의 수 구하기

# ex) n = 15
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

def two_pointer(n):
    num = [i for i in range(1, n+1)]
    
    start, end = 0, 0
    result = 0
    count = 0
    
    while end < n or start < n:
        if result < n:
            result += num[end]
            end += 1
        elif result >= n:
            if result == n:
                count += 1
            result -= num[start]
            start += 1
        # print(start, end, result)
        
    return count
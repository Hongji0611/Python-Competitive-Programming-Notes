import sys

input = sys.stdin.readline

#휴가기간인 V일 내에서 연속하는 P일을 선택했을 때, 캠피장을 이용한 횟수가 L이어야 한다.

count = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    result = 0
    
    result += l * (v // p)
    v %= p
    if v < l:
        result += v
    else:
        result += l
    
    print("Case %d: %d" %(count, result))
    count += 1

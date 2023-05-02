# 30 배수의 공식
# 마지막 자리수가 0이어야 한다.
# 모든 자리수의 합이 3으로 나누어 떨어져야 한다.

n = input()
n = sorted(n, reverse=True)

sum = 0

if '0' not in n:
    print(-1)
else:
    for i in n:
        sum+= int(i)
    if sum % 3 == 0:
        print(''.join(n))
    else:
        print(-1)
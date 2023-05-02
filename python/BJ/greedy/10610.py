# 30 배수의 공식
# 마지막 자리수가 0이어야 한다.
# 모든 자리수의 합이 3으로 나누어 떨어져야 한다.

n = input()

list = list()

for i in range(len(n)):
    list.append(int(n[i]))

list.sort(reverse=True)

result = ""
count = 0
is_zero = 0

for i in list:
    count += i
    result += str(i)
    if i == 0:
        is_zero = 1

if is_zero == 1 and count % 3 == 0:
    print(result)
else:
    print(-1)
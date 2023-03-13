#BJ 10773
import sys
input = sys.stdin.readline

k = int(input())

_list = list()
for _ in range(k):
    num = int(input())
    if num == 0:
        _list.pop()
    else:
        _list.append(num)

print(sum(_list))
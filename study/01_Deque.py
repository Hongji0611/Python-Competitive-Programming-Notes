#BJ 5430
import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    _list = input().rstrip('\n')[1:-1].split(',') 
    if n == 0:
        _list = []
    dq = deque(_list)

    count = 0
    for i in p:
        if i == 'R':
            count += 1
        elif i == 'D':
            if len(dq) == 0:
                print("error")
                break
            else:
                if count % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
    else:
        if count % 2 != 0:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
#큐 구현 - deque

import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

n = int(input())

for _ in range(n):
    line = input().strip().split()
    if line[0] == "push":
        queue.append(line[1])
    elif line[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif line[0] == "size":
        print(len(queue))
    elif line[0] == "empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif line[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif line[0] == "back":
        if queue:
            print(queue[-1]) 
        else:
            print(-1)

#BJ 2164
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
for i in range(1, n+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.rotate(-1)

print(dq[0])
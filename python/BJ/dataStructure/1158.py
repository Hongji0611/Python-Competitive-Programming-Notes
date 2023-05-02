import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque()

for i in range(n):
    q.append(i+1)

print("<", end="")
while len(q) > 0:
    for _ in range(k-1):
        q.append(q.popleft())
    print(q.popleft(), end="")
    if len(q) != 0:
        print(", ", end="")
print(">")

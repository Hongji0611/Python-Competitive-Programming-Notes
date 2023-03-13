#Stack
#-역으로 추적하는 경우, 나중에 들어온 데이터가 빨리 나가야 할 때 사용
#List에 pop으로 사용

#Queue
#-순차적으로 진행되는 일을 스케쥴링할 때 사용
#deque로 사용
from collections import deque
dq = deque('12345')
dq.append(6)
dq.appendleft(0)
dq.pop() #6
dq.popleft() #0
dq.rotate(1) # 5 1 2 3 4



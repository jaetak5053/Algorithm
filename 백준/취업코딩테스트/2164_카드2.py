from collections import deque
dq = deque()
tmp = 0
N = int(input())
for i in range(N, 0, -1):
    dq.append(i)
while (len(dq) != 1):
    dq.pop()

    tmp = dq.pop()
    dq.appendleft(tmp)
print(dq.pop())

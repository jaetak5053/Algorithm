import sys
from collections import deque

for i in range(int(input())):
    dq1 = deque()
    dq2 = deque()
    for j in input():
        if (j == '<'):
            if (len(dq1)):
                dq2.appendleft(dq1.pop())
        elif (j == '>'):
            if (len(dq2)):
                dq1.append(dq2.popleft())
        elif (j == '-'):
            if (dq1):
                dq1.pop()
        else:
            dq1.append(j)
    print(''.join(dq1)+''.join(dq2))

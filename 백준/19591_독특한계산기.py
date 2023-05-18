from collections import deque
Input = input()
dq = deque(Input)
while (1):
    arr_front = []
    arr_tail = []
    for i in range 3:
        arr_front.append(dq.popleft())
        arr_tail.append(dq.pop())
    if (arr_front[1])

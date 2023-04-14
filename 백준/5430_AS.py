import sys
from collections import deque

T = int(input())  # 테스트케이스 개수
for i in range(T):
    p = sys.stdin.readline().rstrip()  # 함수
    n = int(input())  # 배열 내 숫자 개수
    arr = input()[1:-1].split(',')  # 배열
    dq = deque(arr)
    flag = 0
    rev = 0
    front = 0
    back = len(dq)-1
    if n == 0:
        dq = []
        front = 0
        back = 0
    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(dq) < 1:
                flag = 1
                print("error")
                break
            else:
                if (rev % 2 == 0):
                    dq.popleft()
                else:
                    dq.pop()
    if flag == 0:
        if rev % 2 == 0:
            print('['+','.join(dq)+']')
        else:
            dq.reverse()
            print('['+','.join(dq)+']')

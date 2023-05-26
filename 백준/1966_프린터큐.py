import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input())
    cnt = 1
    paper = deque()
    paper.appendleft(int(input().split()) for _ in range(N))

    if max(paper) <= paper[M]:
        print(cnt)
    else:
        x = paper[M]
        paper.pop(paper.index(paper[M]))
        paper.appendleft(x)
        M = len(paper)-1
        cnt += 1

        *******************************************************

from collections import deque
import sys
input = sys.stdin.readline
dy = (-1, -2, -2, -1, 1, 2, 2, 1)
dx = (-2, -1, 1, 2, 2, 1, -1, -2)
S = 0
N = int(input())


def IsValidCoord(y, x):
    return 0 <= y < S and 0 <= x < S


for _ in range(N):
    S = int(input())
    dq = deque()

    start_y, start_x = map(int, input().split())
    goal_y, goal_x = map(int, input().split())
    visited = [[False]*S for _ in range(S)]
    dq.append((start_y, start_x, 0))
    while dq:
        y, x, d = dq.popleft()
        if y == goal_y and x == goal_x:
            print(d)
            break
        for k in range(8):
            ny = y+dy[k]
            nx = x+dx[k]
            nd = d+1
            if IsValidCoord(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((ny, nx, nd))

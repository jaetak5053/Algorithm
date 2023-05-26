import heapq
import sys
input = sys.stdin.readline
N = int(input())
hq = []
for i in range(N):
    for j in map(int, input().split()):
        if (len(hq) >= N):
            heapq.heappushpop(hq, j)
        else:
            heapq.heappush(hq, j)

print(hq[0])

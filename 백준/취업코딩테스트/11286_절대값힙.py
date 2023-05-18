import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

hq = []

for i in range(N):
    if arr[i] == 0:
        print(heapq.heappop(hq)[1] if len(hq) else 0)
    else:
        heapq.heappush(hq, (abs(arr[i]), arr[i]))

print(hq)

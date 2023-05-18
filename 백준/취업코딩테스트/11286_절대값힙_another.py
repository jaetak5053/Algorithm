import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
max_heap = []  # 양수
min_heap = []  # 음수
for i in range(N):
    if (arr[i] < 0):
        heapq.heappush(min_heap, arr[i])
    elif (arr[i] > 0):
        heapq.heappush(max_heap, -arr[i])
    else:
        if (len(min_heap)):
            if (len(max_heap) == 0 or min_heap[0] < max_heap[0]):
                print(heapq.heappop(min_heap))
            else:
                print(-heapq.heappop(max_heap))
        else:
            print(-heapq.heappop(max_heap) if len(max_heap) else 0)

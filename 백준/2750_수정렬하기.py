import sys
N = int(input())
arr = [int(sys.stdin.readline().rstrip()) for i in range(N)]

for i in range(0, N):
    for j in range(0, N-i-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
for i in arr:
    print(i)

from itertools import combinations
# N개의 정수로 이루어진 수열
# 크기가 양수인 부분수열 중 그 수열의 원소를 다 더한값이 S가 되는 경우의 수
N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    subarr = combinations(arr, i)
    for j in subarr:
        if (sum(j) == S):
            cnt += 1

print(cnt)

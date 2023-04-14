N, K = map(int, input().split())
arr = [i+1 for i in range(N)]
ans = []
idx = 0
while (arr):
    idx = (idx+K-1) % len(arr)
    ans.append(str(arr.pop(idx)))
print('<', ', '.join(ans), '>', sep='')

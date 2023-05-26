problem = [False] * 1001
N, L = map(int, input().split())
ans = 0
idx = 0
for i in map(int, input().split()):

    problem[i] = True

while (idx < 1001):
    if problem[idx] == True:
        ans += 1
        idx += L
    else:
        idx += 1
print(ans)

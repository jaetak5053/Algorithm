import sys
input = sys.stdin.readline
ans = dict()
for i in range(int(input())):
    k, v = input().split()
    ans[k] = v

for k, v in sorted(ans.items(), reverse=True):
    if v == 'enter':
        print(k)

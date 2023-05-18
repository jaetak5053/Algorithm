import sys
N = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]


ans = []
for i in arr:

    stk = []
    flag = 0
    for j in range(len(i)):
        if (i[j] == '('):
            stk.append(i[j])
        if (i[j] == ')'):
            if (stk):
                stk.pop()
            else:
                ans.append('NO')
                flag = 1
                break
    if (flag == 1):
        continue
    elif (stk):
        ans.append('NO')
    else:
        ans.append('YES')
print('\n'.join(ans))

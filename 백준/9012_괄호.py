import sys

ans = []

T = int(input())
for i in range(T):
    str = (sys.stdin.readline().rstrip())
    st = []
    flag = 0
    for j in str:
        if (j == '('):
            st.append('j')
        elif (j == ')'):
            if (len(st) == 0):
                ans.append("NO")
                flag = 1
                break
            else:
                st.pop()
    if (len(st) == 0 and flag != 1):
        ans.append("YES")
    elif (flag != 1):
        ans.append("NO")
print('\n'.join(ans))

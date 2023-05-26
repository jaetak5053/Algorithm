N = int(input())
arr = input()
stk = []
val = []
for _ in range(N):
    val.append(int(input()))
for i in arr:
    if i.isalpha():
        stk.append(val[ord(i)-ord('A')])

    else:
        back = stk.pop()
        first = stk.pop()
        if i == '+':
            stk.append(first+back)
        elif i == '-':
            stk.append(first-back)
        elif i == '*':
            stk.append(first*back)
        else:
            stk.append(first / back)
print(f'{stk[0]:.2f}')

import sys
while (True):

    arr = sys.stdin.readline().rstrip()
    flag = 0
    end_flag = 0
    stack = []
    if (arr == '.'):
        break
    for i in arr:
        if i == ".":
            break
        elif i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if (len(stack) == 0):
                flag = 1
                break
            elif (stack[-1] == '('):
                stack.pop(-1)
            else:
                stack.append(i)
        elif i == ']':
            if len(stack) == 0:
                flag = 1
                break
            elif stack[-1] == '[':
                stack.pop(-1)
            else:
                stack.append(i)
    if (flag == 1):
        print('no')
        flag = 0
    elif (len(stack) == 0):
        print('yes')
    else:
        print('no')

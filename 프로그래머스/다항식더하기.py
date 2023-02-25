def solution(polynomial):
    answer = ''
    x_num = 0
    num = 0
    answer = polynomial.split(' + ')
    print(answer)
    for i in answer:
        if ('x' in i):
            a = i.replace('x', '')
            if (a):
                x_num += int(a)
            else:
                x_num += 1

        else:
            num += int(i)
    if ((x_num != 0) and (num != 0)):
        if (x_num == 1):
            return 'x + ' + str(num)
        else:
            return str(x_num) + 'x + ' + str(num)
    elif ((x_num != 0) and (num == 0)):
        if (x_num == 1):
            return 'x'
        else:
            return str(x_num) + 'x'
    else:
        return str(num)

def solution(my_string, num1, num2):
    answer = ''
    print(my_string[num1])
    print(len(my_string))
    tmd = my_string[num1]
    for i in range(len(my_string)):
        if (i == num1):
            a = my_string[num2]
        elif (i == num2):
            a = tmd
        else:
            a = my_string[i]
        answer += a

    return answer

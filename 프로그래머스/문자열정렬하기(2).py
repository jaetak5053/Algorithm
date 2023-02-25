def solution(my_string):
    answer = ''
    list = sorted(my_string.lower())
    for i in list:
        answer += i

    return answer

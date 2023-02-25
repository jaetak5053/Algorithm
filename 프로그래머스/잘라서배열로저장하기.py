def solution(my_str, n):
    answer = []

    for i in range(0, len(my_str), n):
        print(i)
        print(my_str[i:i+n])
        answer.append(my_str[i:i+n])

    return answer

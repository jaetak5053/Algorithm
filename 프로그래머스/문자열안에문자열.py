def solution(str1, str2):
    answer = 0
    str = str1.replace(str2, " ")
    print(str)
    if (str != str1):
        return 1
    else:
        return 2

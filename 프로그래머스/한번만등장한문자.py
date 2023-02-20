def solution(s):
    answer = ''
    count = 0
    s1 = sorted(s)
    for i in s1:
        if s.count(i) == 1:
            answer += i

    return answer

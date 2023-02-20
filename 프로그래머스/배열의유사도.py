def solution(s1, s2):
    answer = set(s1) & set(s2)

    return len(answer)

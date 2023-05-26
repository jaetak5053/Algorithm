import sys
sys.setrecursionlimit(10**6)


def solution(chicken):
    answer = 0
    c = chicken
    if c < 10:
        return 0
    while (c > 9):

        l = c % 10
        s_c = c // 10
        answer += s_c
        c = (s_c+l)
        print(f'c={c} s_c={s_c} answer = {answer}')

    return answer

def solution(sides):
    answer = 0
    answer += (max(sides)+min(sides))-max(sides)
    answer += max(sides)-(max(sides)-min(sides)+1)
    return answer

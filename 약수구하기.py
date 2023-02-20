def solution(n):
    answer = [1,]
    a = n
    for i in range(2, n+1):
        if (a % i == 0):
            answer.append(i)
    return answer

import math


def fact(n):
    if n == 1:
        return 1
    return n*fact(n)


def solution(n):
    answer = 0
    for i in range(1, 11):
        if math.factorial(i) > n:
            return i-1
        elif math.factorial(i) == n:
            return i

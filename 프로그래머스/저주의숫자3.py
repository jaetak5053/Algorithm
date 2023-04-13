def HaveThree(n):
    s = str(n)
    if s.count('3') == 0:
        return 1
    else:
        return 0


def solution(n):
    answer = 0
    num_list = []
    for i in range(1, 200):
        if (i % 3 != 0):
            if (HaveThree(i)):
                num_list.append(i)
    print(num_list)
    return num_list[n-1]

def solution(array):
    answer = []
    maxim = max(array)
    max_idx = array.index(max(array))
    answer.append(maxim)
    answer.append(max_idx)
    return answer

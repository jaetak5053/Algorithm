def solution(keyinput, board):
    answer = [0, 0]
    board_lr = (board[0]-1)/2
    board_ud = (board[1]-1)/2
    for i in keyinput:
        if (i == "left"):
            if (-board_lr < answer[0] <= board_lr):
                answer[0] -= 1
        elif (i == "right"):
            if (-board_lr <= answer[0] < board_lr):
                answer[0] += 1
        elif (i == "up"):
            if (-board_ud <= answer[1] < board_ud):
                answer[1] += 1
        elif (i == "down"):
            if (-board_ud < answer[1] <= board_ud):
                answer[1] -= 1

    return answer

def solution(board):
    answer = 0
    num1 = len(board)
    num2 = len(board[0])
    comp = [[1 for i in range(num2+1)] for j in range(num1+1)]
    print(comp)

    for i in range(num1):
        for j in range(num2):
            comp[i][j] = board[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if (i == 0):
                    if (j == 0):
                        comp[i+1][j+1] = 2
                        comp[i+1][j] = 2
                        comp[i][j+1] = 2
                    elif (j == len(board[i])-1):
                        comp[i+1][j] = 2
                        comp[i][j-1] = 2
                        comp[i+1][j-1] = 2
                    else:
                        comp[i][j-1] = 2
                        comp[i][j+1] = 2
                        comp[i+1][j-1] = 2
                        comp[i+1][j] = 2
                        comp[i+1][j+1] = 2
                elif (i == len(board)-1):
                    if (j == 0):
                        comp[i][j+1] = 2
                        comp[i-1][j] = 2
                        comp[i-1][j+1] = 2
                    elif (j == len(board[i])-1):
                        comp[i][j-1] = 2
                        comp[i-1][j] = 2
                        comp[i-1][j-1] = 2
                    else:
                        comp[i][j-1] = 2
                        comp[i][j+1] = 2
                        comp[i-1][j-1] = 2
                        comp[i-1][j] = 2
                        comp[i-1][j+1] = 2
                else:
                    comp[i-1][j-1] = 2
                    comp[i-1][j] = 2
                    comp[i-1][j+1] = 2
                    comp[i][j-1] = 2
                    comp[i][j+1] = 2
                    comp[i+1][j-1] = 2
                    comp[i+1][j] = 2
                    comp[i+1][j+1] = 2
    print(comp)
    print(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if comp[i][j] == 0:
                answer += 1

    return answer

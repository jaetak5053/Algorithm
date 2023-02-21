def valid(quiz):
    quiz = quiz.replace('=', '==')
    print(quiz)
    return eval(quiz)


def solution(quizs):
    return ["O" if valid(quiz) else "X" for quiz in quizs]

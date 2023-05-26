import sys
input = sys.stdin.readline
N = int(input())
T = [i*(i+1)//2 for i in range(49)]


def IsCorrect(K):
    for i in range(1, 49):
        for j in range(i, 49):
            for k in range(j, 49):
                if T[i] + T[j] + T[k] == K:
                    return 1
    return 0


for i in range(N):
    print(IsCorrect(int(input())))

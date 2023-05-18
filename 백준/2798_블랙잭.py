import sys


def ans(card, N):
    sum = 0
    for i in range(N):
        if M < card[i]:
            continue
        for j in range(i+1, N):
            if (M < (card[i]+card[j])):
                continue
            for k in range(j+1, N):

                if (M < (card[i]+card[j]+card[k])):
                    continue
                if sum < card[i]+card[j]+card[k]:
                    sum = card[i]+card[j]+card[k]
    return sum


N, M = map(int, input().split())
card = list(map(int, sys.stdin.readline().split()))
card.sort(reverse=True)
print(ans(card, N))

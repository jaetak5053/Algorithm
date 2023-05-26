from bisect import bisect_left, bisect_right
N = int(input())
cards = sorted(map(int, input().split()))
ans = []
M = int(input())
x = list(map(int, input().split()))

for i in range(M):
    ans.append(bisect_right(cards, x[i]) - bisect_left(cards, x[i]))


print(' '.join(map(str, ans)))

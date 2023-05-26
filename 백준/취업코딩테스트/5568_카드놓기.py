from itertools import permutations

n = int(input())
k = int(input())
card = []
for i in range(n):
    card.append(int(input()))
s = set()
for i in permutations(card, k):
    a = ''
    for j in range(k):
        a += str(i[j])
    s.add(a)
print(len(s))

# (1,2)
# (12,1)
# (2,1)


# 21 212 121 12 112 11

# 1 2 12 1
# 12 112 11 21 212 121 122

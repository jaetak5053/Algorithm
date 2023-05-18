from itertools import combinations
list = []
flag = 0
for i in range(9):
    list.append(int(input()))
for combi in combinations(list, 7):
    if sum(combi) == 100:
        for i in sorted(combi):
            print(i)
        break

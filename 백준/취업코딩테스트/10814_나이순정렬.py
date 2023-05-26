import sys
input = sys.stdin.readline
N = int(input())
people = []
order = 0
ans = []
for _ in range(N):
    order += 1
    age, name = input().split()
    people.append((int(age), order, name))
people.sort()

for i in people:
    print(f'{i[0]} {i[2]}')

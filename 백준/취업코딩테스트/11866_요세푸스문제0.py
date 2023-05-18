N, K = map(int, input().split())
people = []
for i in range(N):
    people.append(i+1)
ptr = 0
ans = []
while (people):
    ptr = (ptr+K-1) % len(people)
    ans.append(str(people.pop(ptr)))


print('<' + ', '.join(ans) + '>')

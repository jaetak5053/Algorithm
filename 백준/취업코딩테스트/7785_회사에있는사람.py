import sys
input = sys.stdin.readline
s = set()
for i in range(int(input())):
    name, state = input().split()
    if state == 'enter':
        s.add(name)
    else:
        s.remove(name)
for i in sorted(s, reverse=True):
    print(i)

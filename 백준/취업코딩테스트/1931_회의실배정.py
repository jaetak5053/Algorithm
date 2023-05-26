import sys
input = sys.stdin.readline
N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((end, start))
t = 0
ans = 0
meetings.sort()
for end, start in meetings:
    if t <= start:
        ans += 1
        t = end
print(ans)

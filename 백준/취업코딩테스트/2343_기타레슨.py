
N, M = map(int, input().split())
lesson = list(map(int, input().split()))
lo = max(lesson)
hi = sum(lesson)
mid = (lo+hi)//2
ans = hi


def func(x):
    cnt = 1
    bluray = 0
    for i in lesson:
        if bluray + i <= x:
            bluray += i

        else:
            cnt += 1
            bluray = i
    return cnt <= M


while lo <= hi:
    if func(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid+1
    mid = (lo+hi) // 2
print(ans)

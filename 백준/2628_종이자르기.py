x, y = map(int, input().split())
garo = [0, x]
sero = [0, y]
cut_times = int(input())
for i in range(cut_times):
    num, line_num = map(int, input().split())
    if (num == 0):
        sero.append(line_num)
    else:
        garo.append(line_num)
garo = sorted(garo)
sero = sorted(sero)
result_list = []
for i in range(1, len(garo)):
    for j in range(1, len(sero)):
        width = garo[i]-garo[i-1]
        height = sero[j]-sero[j-1]
        result_list.append(width*height)
print(max(result_list))

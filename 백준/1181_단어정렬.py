N = int(input())
word_list = []

for i in range(1, N+1):
    word_list.append(input())
set_word_list = set(word_list)
removed_word_list = list(set_word_list)
removed_word_list.sort()
removed_word_list.sort(key=len)
for i in removed_word_list:
    print(i)

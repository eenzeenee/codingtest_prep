# 단어 정렬

#%%
N = int(input())
words = []

for _ in range(N):
    word = input()
    if [len(word), word] not in words:
        words.append([len(word), word])

for i, word in sorted(words):
    print(word)
# %%

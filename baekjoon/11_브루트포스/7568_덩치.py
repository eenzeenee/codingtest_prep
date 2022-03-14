# 7568 덩치

#%%
N = int(input())

person = []

for _ in range(N):
    weight, height = map(int, input().split())
    person.append((weight, height))

ranks = []

for i in range(len(person)):
    rank = 1
    mine = person[i]
    for j in range(len(person)):
        other = person[j]
        if mine[0] < other[0] and mine[1] < other[1]:
            rank += 1
    ranks.append(rank)

for i in ranks:
    print(i, end = ' ')

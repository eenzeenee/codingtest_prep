# 나이 순 정렬

#%%
N = int(input())
members = dict()

for _ in range(N):
    age, name = input().split()
    members[name] = int(age)

members = sorted(members.items(), key = lambda x : x[1])

for name, age in members:
    print(age, end = ' ')
    print(name)

## 왜 틀렸을까????
# %%
N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name])

members = sorted(members, key = lambda x: x[0])

for age, name in members:
    print(age, end = ' ')
    print(name)
# %%

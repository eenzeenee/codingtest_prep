# 좌표 정렬하기

#%%
N = int(input())
answer = list()

for _ in range(N):
    num = list(map(int, input().split()))
    answer.append(num)

answer.sort()       # 2차원 리스트에서 Sort함수를 사용하면 y값까지 알아서 정렬해줌

for num, idx in answer:
    print(num, end = ' ')
    print(idx)

# %%
### 왜 틀렸을까?

N = int(input())
answer = dict()

for _ in range(N):
     x, y = map(int, input().split())
     answer[y] = x

answer = dict(sorted(answer.items()))   # 딕셔너리는 key, value 중 한가지 기준으로만 정렬 가능하기 때문에!!!

for idx in answer:
    print(answer[idx], idx)
# %%

# 좌표 압축

#%%
import sys
N = int(input())
answers = list(map(int, sys.stdin.readline().split()))
sorted_answers = list(set(answers))
sorted_answers.sort()

for i in answers:
    print(sorted_answers.index(i), end = ' ')

## 시간초과
## 리스트 index 찾는 과정에서 시간 많이 소요됨
# %%
import sys
N = int(input())
answers = list(map(int, sys.stdin.readline().split()))
sorted_answers = list(set(answers))
sorted_answers.sort()

idx_dict = {sorted_answers[i] : i for i in range(len(sorted_answers))}

for num in answers:
    print(idx_dict[num], end = ' ')

## 숫자 : 인덱스 딕셔너리 만들어서 인덱스 찾는 시간 줄임
# %%

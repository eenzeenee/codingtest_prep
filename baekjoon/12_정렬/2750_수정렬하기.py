# 수 정렬하기
#%%
N = int(input())
answer = []
for _ in range(N):
    num = int(input())
    answer.append(num)

## 버블 정렬 - 앞에서부터 시작해서 큰 수를 뒤로 보내기
for i in range(N-1):
    for j in range(N-i-1):
        if answer[j] > answer[j+1]:
            answer[j], answer[j+1] = answer[j+1], answer[j]
            

## 삽입 정렬
for i in range(1, N):
    for j in range(i, 0, -1):       # i번째부터 처음으로 (역순)
        if answer[j-1] > answer[j]:
            answer[j-1], answer[j] = answer[j], answer[j-1]

for i in answer:
    print(i)
# %%

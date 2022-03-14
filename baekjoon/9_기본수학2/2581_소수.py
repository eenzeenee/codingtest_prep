# M 이상 N 이하의 소수 합계, 최솟값 찾기

#%%
M = int(input())
N = int(input())

answers = []

for i in range(M, N+1):
    num = 0

    for j in range(2, i + 1):       
        # 1로 시작하는 경우를 신경쓰지 않아도 됨!
        # range 함수는 어차피 정해진 방향으로 흐르기 때문에
        if i % j == 0:
            num += 1
    if num == 1:
        answers.append(i)

if answers == []:
    print(-1)
else:
    print(sum(answers))
    print(answers[0])
# %%

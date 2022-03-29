#%%
def solution(answers):
    answer = []
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(len(answers)):
        idx_1 = i % len(answer_1)
        idx_2 = i % len(answer_2)
        idx_3 = i % len(answer_3)
        if answers[i] == answer_1[idx_1]:
            num1 += 1
        if answers[i] == answer_2[idx_2]:
            num2 += 1
        if answers[i] == answer_3[idx_3]:
            num3 += 1
    max_num = max(num1, num2, num3)
    if max_num == num1:
        answer.append(1)
    if max_num == num2:
        answer.append(2)
    if max_num == num3:
        answer.append(3)
    return answer
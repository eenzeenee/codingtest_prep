#%%
def solution(progresses, speeds):
    tmp = []
    answer = []
    for p, s in zip(progresses, speeds):
        if (100-p) % s != 0:
            tmp.append(((100-p) // s) + 1)
        else:
            tmp.append((100-p) // s)
    print(tmp)
    new_tmp = [tmp[0]]
    for i in range(1, len(tmp)):
        if tmp[i] > tmp[i-1] and tmp[i] > max(new_tmp):
            answer.append(len(new_tmp))
            new_tmp = [tmp[i]]
        else:
            new_tmp.append(tmp[i])
        print(new_tmp)  
    if new_tmp != []:
        answer.append(len(new_tmp))
    
    return answer
#%%

a = [96, 99, 98, 97]
b = [1, 1, 1, 1]
solution(a, b)

## 이 경우 tmp = [4, 1, 2, 3] 으로 나와서 
# line 13의 조건을 tmp[i] > tmp[i-1] 이것만 사용할 경우
# [2, 1, 1] 이 정답으로 나옴 -> 이를 해결하기 위해 tmp[i] > max(new_tmp) 이 조건 또한 추가함
# %%

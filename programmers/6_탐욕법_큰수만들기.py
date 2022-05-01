#%%
def solution(number, k):
    from itertools import combinations
    nums = [int("".join(i)) for i in combinations(number, len(number)-k)]
    
    answer = str(max(nums))
    return answer
# 시간초과

#%%

def solution(number, k):
    length = len(number) - k
    answer = []
    end = len(number) - length + 1
    
    while len(answer) != length:
        temp = '0'
        print(number, end)
        for i in range(len(number[0:end])):
            if number[i] > temp:
                temp = number[i]
                p = i
                if number[i] == '9':
                    break
        if temp == '0':
            p = 0
        answer.append(temp)
        number = number[p+1:]
        end = len(number) - length + 1 + len(answer)
    
    answer = ''.join(answer)
    return answer

# 실패 : 출력크기 초과
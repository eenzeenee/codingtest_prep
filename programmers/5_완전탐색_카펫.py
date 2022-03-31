#%%
def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow/2)+2): # +2하는 이유 : +1만 하는 경우 yellow가 1인 경우 for문을 돌지 못하고 빈 리스트 반환
        if yellow % i == 0:
            M = i
            N = int(yellow / i)
            
            if (M+N+2)*2 == brown:
                answer = [N+2, M+2]
                break
    
    return answer
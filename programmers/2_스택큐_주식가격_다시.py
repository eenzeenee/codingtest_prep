#%%
def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]  # 마지막 인덱스까지 남은 시간
    stack = [0]                                             # 가격이 하락하지 않은 동안의 인덱스 저장
    for i in range(1, len(prices)):
        idx = stack[-1]                                     # 비교하고자 하는 인덱스 (가격이 떨어지지 않은 마지막 값)
        while stack:
            if prices[idx] > prices[i]:                     # 비교하고자 하는 인덱스의 값이 현재 값보다 크면 (가격이 떨어졌다면)
                answer[idx] = i - idx                       # 가격이 떨어진 때 까지의 시간 계산
                stack.pop()                                 # 가격이 떨어졌으므로 stack에서 인덱스 제거 - stack에는 가격이 떨어지지 않은 인덱스만 저장되어야 함
            else:                                           # 가격이 떨어지지 않았다면
                break                                       # 반복문 탈출
        stack.append(i)                                     # stack에 현재 인덱스 추가하여 비교군으로 만들어주기
    return answer

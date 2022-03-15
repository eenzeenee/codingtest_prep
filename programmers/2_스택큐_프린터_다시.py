# 스택 큐 - 프린터 다시 

#%%
def solution(priorities, location):

    answer = 0
    m = max(priorities)

    while True:

        p = priorities.pop(0)   # 현재 대기열에 있는 문서 추출

        if m == p:              # 현재 대기열에 있는 문서의 우선순위가 가장 높다면

            answer += 1         # 출력

            if location == 0:   # 출력한 문서가 내가 찾던 문서라면
                break           # 반복문 탈출

            else:               # 그렇지 않다면
                location -= 1   # 내가 찾고자 하는 문서 앞의 문서가 출력되었으므로 내 위치 한 칸 앞으로 이동

            m = max(priorities)

        else:                   # 현재 대기열에 있는 문서의 우선순위가 가장 높은 것이 아니라면

            priorities.append(p)# 프린트 대기열의 가장 마지막으로 이동

            if location == 0:   # 문서가 가장 뒤로 옮겨갔지만, 내가 찾던 문서의 위치라면 
                location = len(priorities) - 1  # 이를 문서 대기열의 가장 마지막으로 이동시킴

            else:               # 내가 찾고자 하는 문서가 아니라면
                location -= 1   # 내 위치 한 칸 앞으로 이동
    return answer
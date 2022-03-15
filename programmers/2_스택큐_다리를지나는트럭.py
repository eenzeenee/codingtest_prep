# 다리를 지나는 트럭

#%% 

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length                            # 빈 다리 만들기

    while len(bridge):                                      # 다리가 존재한다면
        answer += 1                                         # 시간 +1초
        bridge.pop(0)                                       # 다리 가장 앞에 있는 차 내보내기
        
        if truck_weights != []:                             # 다리 건너야 할 트럭이 존재한다면
            if sum(bridge) + truck_weights[0] <= weight:    # 다리 위의 무게와 트럭의 무게가 감당 가능하면
                bridge.append(truck_weights.pop(0))         # 다리 위에 트럭 보내기
            else:                                           # 아니라면
                bridge.append(0)                            # 0 보내기
    return answer

## 시간 초과
## 매번 sum 계산하는 과정에서 시간이 초과됨 - 이를 해결하기 위해서는 다리 위의 무게를 재는 추가 변수 필요
#%%

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length    
    sum_bridge = 0                                          # 다리 위 무게 재기 위한 변수

    while len(bridge):
        answer += 1
        sum_bridge -= bridge[0]                             # 다리에서 나간 차 무게 빼기
        bridge.pop(0)

        if bridge != []:
            if sum_bridge + truck_weights[0] <= weight:
                sum_bridge += truck_weights[0]              # 다리에 들어온 차 무게 더하기
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    
    return answer

# 3배 이상 시간 단축됨
#%%

def solution(numbers):
    numbers = [str(X) for X in numbers]
    
    numbers = sorted(numbers, key = lambda x : x*3)         # 문자열 변환 후 3자리로 맞춰준 뒤 각 자리별로 문자열 대소 비교
                                                            # 이를 통해 3이 310보다 앞에 나와야 더 큰 수가 되는 것을 확인 가능
    answer = ''.join(numbers[::-1])                         # sorted의 결과는 작은 수부터 나열되므로 내림차순 정렬을 위해 거꾸로 join
    return str(int(answer))                                 # 0000인 경우 0으로 출력할 수 있도록 정수 변환 뒤 다시 문자열로 변환
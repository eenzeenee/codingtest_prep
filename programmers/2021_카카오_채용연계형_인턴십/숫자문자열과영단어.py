def solution(s):
    answer = ''
    
    answer_dict = {'one':1,
                  'two':2,
                  'three':3,
                  'four':4,
                  'five':5,
                  'six':6,
                  'seven':7,
                  'eight':8,
                  'nine':9,
                  'zero':0}
    tmp = ''
    for k in s:
        tmp += str(k)
        try:
            answer += str(int(tmp))
            tmp = ''
        except:
            if tmp in answer_dict:
                answer += str(answer_dict[tmp])
                tmp = ''
            else:
                pass
    return int(answer)
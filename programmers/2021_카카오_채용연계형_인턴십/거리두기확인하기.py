#%%
from itertools import combinations
def solution(places):
    answer = []
    for place in places:
        person = []
        partition = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    person.append((i,j))
                elif place[i][j] == 'X':
                    partition.append((i,j))
        p = list(combinations(person,2))
        p1 = [k for k in p if (abs(k[0][0]-k[1][0])+abs(k[0][1]-k[1][1])) == 1]
        if p1 != []:
            answer.append(0)
            pass
        p2 = [k for k in p if (abs(k[0][0]-k[1][0])+abs(k[0][1]-k[1][1])) == 2]
        tmp = 0
        for a, b in p2:
            if a[0] == b[0]:
                if (a[0], a[1]+1) not in partition:
                    pass
            elif a[1] == b[1]:
                if (a[0]+1, a[1]) not in partition:
                    pass
            elif sum(a) == sum(b):
                if ((a[0]+1, a[1]) not in partition) or ((a[0], a[1]-1) not in partition):
                    pass
            else:
                if ((a[0]+1, a[1]) not in partition) or ((a[0], a[1]+1) not in partition):
                    pass
            tmp += 1
        try:
            if tmp / len(p2) != 1:
                answer.append(0)
                pass
            else:
                answer.append(1)
        except:
            pass
                    
    return answer

## 3.6/100

#%%
def solution(places):
    answer = []
    persons = []
    parts = []
    for i in range(5):
        person = []
        part = []
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    person.append((j,k))
                elif places[i][j][k] == 'X':
                    part.append((j,k))
        persons.append(person)
        parts.append(part)
        
    for person in persons:
        for a in range(len(person)):
            for b in range(i+1, len(person)):
                if abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1:
                    answer.append(0)
                elif abs(a[0]-b[0]) + abs(a[1]-b[1]) == 2:
                    
                
                
    return answer
## O를 기준으로 생각해보자~

#%%
def solution(places):
    answer = []
    for place in places:
        result = check_func(place)
        answer.append(result)
    return answer

def check_func(place):
    answer = 0
    num_P = 0
    num_O = 0
    for i in range(len(place)):
        for j in range(len(place[i])):
            tmp = ''
            try:
                tmp += place[i+1][j]
            except:
                tmp = tmp
            try:
                tmp += place[i-1][j]
            except:
                tmp = tmp
            try:
                tmp += place[i][j+1]
            except:
                tmp = tmp
            try:
                tmp += place[i][j-1]
            except:
                tmp = tmp
                
            if place[i][j] == 'P':
                num_P += 1
                if 'P' not in tmp:
                    answer += 1
                    
            if place[i][j] == 'O':
                num_O += 1
                if tmp.count('P') < 2:
                    answer += 1
    if answer / (num_P + num_O) == 1:
        return 1
    else:
        return 0
## answer와 num_P + num_O 사이에 차이 발생
## i = 0일 때 place[i-1][j] -> place[-1][j]로 존재하는 거처럼 나옴
## 인덱스 정확히 명시하여 해결해야 함

#%%
def solution(places):
    answer = []
    for place in places:
        result = check_func(place)
        answer.append(result)
    return answer

def check_func(place):
    for i in range(5):
        for j in range(5):
            tmp = ''
            if i != 0:
                tmp += place[i-1][j]
            if i != 4:
                tmp += place[i+1][j]
            if j != 0:
                tmp += place[i][j-1]
            if j != 4:
                tmp += place[i][j+1]
                
            if place[i][j] == 'P':
                if 'P' in tmp:
                    return 0
                    
            if place[i][j] == 'O':
                if tmp.count('P') >= 2:
                    return 0
    return 1
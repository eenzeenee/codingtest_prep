# 수 정렬하기

#%%
import sys
N = int(input())

counting_list = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())     ## input 시간초과 나면 이 코드로 해결하기!!!!!!
    counting_list[num] += 1

for i in range(10001):
    if counting_list[i] != 0:
        for _ in range(counting_list[i]):
            print(i)


#%%
## 계수 정렬 (counting sort)
# 입력 숫자의 범위가 적을 경우 모든 범위에 대해 숫자의 빈도 확인

def counting_sort(array):
    # counting_array 생성
    counting_array = [0] * 10001
    # counting_array에 input array 내 원소의 빈도수 담기
    for i in array:
        counting_array[i] += 1
    
    # counting array 업데이트 : 앞의 빈도수 더해서 누적합으로 만들기
    for i in range(10000):
        counting_array[i+1] += counting_array[i]
    
    # output array 생성
    output_array = [-1] * len(array)

    # output array에 정렬하기 (counting array 참조하여)
    for i in array:
        output_array[counting_array[i] - 1] = i # counting_array가 N개 있을 것이므로 리스트 인덱스는 N-1로 맞추기
        counting_array[i] -= 1

    return output_array

for i in counting_sort(answer):
    print(i)
# %%

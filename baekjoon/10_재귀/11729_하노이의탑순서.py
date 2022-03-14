# 11729 하노이의 탑 순서

### 하노이의 탑 : n개의 원판을 A에서 C로 옮기기 : n, A, C
##### 1) n개의 원판이 주어지면, n-1개의 원판을 B번에 순서대로 정렬하는 것이 중요함 : n-1, A, B
##### 2) 이후 n번째 원판을 C로 옮기기 : A -> C
##### 3) 이후 B에 있던 n-1개의 원판을 C로 순서대로 옮기기 : n-1, B, C
### -> 재귀 함수 사용하여 1), 3) 해결 가능

#%%
def hanoi(n, start, end):
    
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, 6 - (start + end))
    print(start, end)
    hanoi(n-1, 6 - (start + end), end)

n = int(input())

print(2**n - 1)     ### 총 횟수 : 2 ** n - 1 : 실제로 숫자 넣어서 찍어봄
hanoi(n, 1, 3)
# %%
# 01 타일

#%%
import sys
N = int(sys.stdin.readline())

l = [0]*1000001         #### 공간을 미리 할당 ~ append 사용하는 경우 공간을 다시 할당해야하는 비효율 발생하므로
l[1] = 1
l[2] = 2

for i in range(3, N+1):
    num = l[i-1] + l[i-2]
    l[i] = num % 15746              #### N까지 모두 계산한 뒤에 15746으로 나누려고 하면 메모리 초과 발생 ~ 미리 나눠서 넣기

print(l[N])
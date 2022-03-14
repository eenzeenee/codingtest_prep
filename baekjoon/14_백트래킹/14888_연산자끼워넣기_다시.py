# 연산자 끼워넣기
#%%
N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_num = 1000000000
max_num = -1000000000

def find_min_max(depth, num, plus, minus, multiply, devide):
    global min_num, max_num
    if depth == len(nums):          ## 백트래킹 탈출 위한 조건
        min_num = min(num, min_num)
        max_num = max(num, max_num)
        return
    
    if plus:
        find_min_max(depth+1, num + nums[depth], plus-1, minus, multiply, devide)
    if minus:
        find_min_max(depth+1, num - nums[depth], plus, minus-1, multiply, devide)
    if multiply:
        find_min_max(depth+1, num * nums[depth], plus, minus, multiply-1, devide)
    if devide:
        if num >= 0:
            find_min_max(depth+1, num // nums[depth], plus, minus, multiply, devide-1)
        else:
            find_min_max(depth+1, -(-num // nums[depth]), plus, minus, multiply, devide-1)

find_min_max(1, nums[0], operators[0], operators[1], operators[2], operators[3])

print(max_num)
print(min_num)
# %%

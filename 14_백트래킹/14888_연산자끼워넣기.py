# 연산자 끼워넣기

#%%
# import sys
# N = int(sys.stdin.readlines())
# nums = list(map(int, sys.stdin.readlines().split()))
# operators = list(map(int, sys.stdin.readlines().split()))

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

def max_min_op(depth, num, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == N:
        max_num = max(num, max_num)
        min_num = min(num, min_num)
        return
    
    if plus:
        max_min_op(depth+1, num + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        max_min_op(depth+1, num - nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        max_min_op(depth+1, num * nums[depth], plus, minus, multiply-1, divide)
    if divide:
        if num >= 0:
            max_min_op(depth+1, num // nums[depth], plus, minus, multiply, divide-1)
        else:
            max_min_op(depth+1, -1*(-num // nums[depth]), plus, minus, multiply, divide-1)
    # if divide:
    #     max_min_op(depth+1, int(num / nums[depth]), plus, minus, multiply, divide-1)

max_min_op(1, nums[0], operators[0], operators[1], operators[2], operators[3])

print(max_num)
print(min_num)

# %%

# 신나는 함수 실행
#%%

def func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    else:
        return func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
    
# %%
func(50, 50, 50)
# %%
import sys
log = {}

def func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    
    key = '{} {} {}'.format(a, b, c)

    if key in log:
        return log[key]
    res = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
    log[key] = res
    return res

while True:
    # a, b, c = map(int, sys.stdin.readline().split())
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    
    print('w({}, {}, {}) = {}'.format(a, b, c, func(a,b,c)))

# %%

import sys

log = dict()

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    key = f'{a} {b} {c}'

    if key in log:
        return log[key]
    
    res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    log[key] = res
    return res

while True:
    a, b, c = list(map(int, sys.stdin.readline().split()))      ## split 까먹지 말자!
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
# %%

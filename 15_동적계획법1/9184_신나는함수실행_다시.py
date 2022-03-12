# 신나는 함수 실행 다시 풀어보기
#%%
import sys
log = dict()

def w(a, b, c):
    if a <= 0 and b <= 0 and c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    else:

        key = f'{a} {b} {c}'
        if key in log:
            return log[key]
        
        res = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        log[key] = res
        return res

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')

# 직각삼각형

#%%
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    [a, b, c] = sorted([a,b,c])
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')
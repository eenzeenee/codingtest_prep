# 터렛

#%%

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    if (x1 == x2) and (y1 == y2) and (r1 == r2):
        print(-1)
    elif (r1 + r2 < dist) or ((x1 == x2) and (y1 == y2) and (r1 != r2)) or (dist > r1) or (dist > r2):
        print(0)
    elif r1 + r2 == dist:
        print(1)
    else:
        print(2)
    
    
# %%
T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if (dist == 0) and (r1 == r2):
        print(-1)
    elif (abs(r1 - r2) == dist) or (r1 + r2 == dist):
        print(1)
    elif (dist > r1 + r2) or (r2 > dist + r1) or (r1 > dist + r2):
        print(0)
    else:
        print(2)

## 2 점에서 만나는 경우
#### if (abs(r1 - r2) < dist < (r1 + r2)):
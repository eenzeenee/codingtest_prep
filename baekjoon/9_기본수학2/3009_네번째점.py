# 네번째 점
#%%

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

answer = []

if x1 == x2:
    answer.append(x3)
elif x1 == x3:
    answer.append(x2)
else:
    answer.append(x1)

if y1 == y2:
    answer.append(y3)
elif y1 == y3:
    answer.append(y2)
else:
    answer.append(y1)

print(answer[0], answer[1])


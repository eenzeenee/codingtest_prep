# 달팽이는 올라가고 싶다

A, B, V = input().split()

import math

print(math.ceil((int(V) - int(A)) / (int(A) - int(B)) + 1))

## 낮에도 올라갈 수 있으니까 마지막 하루 낮에 올라간 내용 미리 빼고 시작하기 : int(V) - int(A)
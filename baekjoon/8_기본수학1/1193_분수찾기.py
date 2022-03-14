# 분수찾기

A = int(input())
n = 1
while True:
    A -= n
    if A <= 0:# 분모가 0이 되면 안되므로 <= 등호 필수
        A += n
        break
    else:
        n += 1
if n % 2:
    print(str(n + 1 - A)+ '/' + str(A))
else:
    print(str(A)+ '/' + str(n + 1 - A))
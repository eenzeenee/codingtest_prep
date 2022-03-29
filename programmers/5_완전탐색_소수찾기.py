#%%

def solution(numbers):
    answer = 0
    from itertools import permutations
    nums = []
    for i in range(1, len(numbers) + 1):
        tmp = [int(''.join(l)) for l in permutations(numbers, i)]
        nums+=tmp
    nums = set(nums)
    #print(nums)
    
    import math
    for num in nums:
        no_prime = 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                no_prime += 1
        if no_prime == 0 and num >= 2:
            #print(num)
            answer += 1
                

    return answer

#%%
# 보다 효율적인 코드 구현 위해서
# 에라토스테네스의 체 구현
# 에라토스테네스의 체 : 2의 배수 지우기 -> 3의 배수 지우기 -> 5의 배수 지우기 ...
def solution(numbers):
    from itertools import permutations
    nums = set()
    for i in range(len(numbers)):
        nums |= set(map(int, map("".join, permutations(list(numbers), i+1))))
    nums -= set(range(0,2))
    max_num = max(nums)
    for i in range(2, int(len(nums)**0.5) + 1):
        nums -= set(range(i*2, max_num+1, i))
    # print(nums)
    return len(nums)

### 이 경우 실패 발생 -> max_num 값이 차집합 과정에서 변화하는 내용 따라서 계속 변화해야 함

#%%
def solution(numbers):
    from itertools import permutations
    nums = set()
    for i in range(1, len(numbers)+1):
        nums |= set(map(int, map("".join, permutations(list(numbers), i)))) # 만들 수 있는 모든 수의 조합을 합집합
    
    nums -= set(range(0, 2))        # 0, 1은 소수가 아니므로 삭제

    for i in range(2, int(max(nums) ** 0.5)+1):
        nums -= set(range(i*2, max(nums)+1, i))     # 에라토스테네스의 체 : i의 2배부터 최댓값까지 i 간격으로 집합 구해서 제외시키기

    return len(nums)
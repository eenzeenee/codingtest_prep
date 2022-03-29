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


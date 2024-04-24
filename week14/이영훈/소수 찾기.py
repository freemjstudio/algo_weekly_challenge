from itertools import permutations, combinations

cnt = 0

def is_sosu(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    arr = set()
    for i in range(1, len(numbers) + 1):
        combi = list(combinations(numbers, i))
        for comb in combi:
            permu = list(permutations(comb))
            for p in permu:
                arr.add(int(''.join(p)))
     
    for num in arr:
        if is_sosu(num):
            answer += 1
    
    print(arr)
    return answer
    
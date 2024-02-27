from itertools import combinations
from functools import reduce
def solution(N):
    target = 10
    num = [i for i in range(1,N+1)]
    max_N = 0
    count = 0
    for i in range(1,N+1):
        count += i
        if count == target:
            max_N = i
            break
            
    combi = []    
    for i in range(2,max_N+1):
        com = combinations(num, i)
        for c in com:
            c_sum = reduce(lambda x, y: x + y, c)
            if c_sum > target:
                continue
            if c_sum == target:
                combi.append(list(c))
    return sorted(combi)
    

print(solution(5)) 
print(solution(2)) 
print(solution(7))

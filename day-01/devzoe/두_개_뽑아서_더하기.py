from itertools import combinations

def solution(numbers):
    c = list(set([x+y for x, y in combinations(numbers, 2)]))
    c.sort()
    
    return c

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))

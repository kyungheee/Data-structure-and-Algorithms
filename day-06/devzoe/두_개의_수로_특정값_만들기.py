from itertools import combinations
def solution(arr, target):
    c = combinations(arr, 2)
    for i in c:
        if i[0]+i[1] == target:
            return True
    return False
print(solution([1,2,3,4,8],6))
print(solution([2,3,5,9],10))

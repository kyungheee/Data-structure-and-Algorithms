def solution(nums):
    result = 0
    n = set(nums)
    length = len(nums) / 2
    if len(n) >= length:
        result = length
    else:
        result = len(n)
    return result

def solution(arr):
    lst= list(set(arr))
    lst.sort(reverse=True)
    return lst
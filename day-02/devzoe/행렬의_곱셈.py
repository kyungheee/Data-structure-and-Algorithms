def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]  
    for i, a1 in enumerate(arr1):
        for j, a2 in enumerate(arr2):
            for k, v in enumerate(a2):
                answer[i][k] += a1[j] * v
    return answer

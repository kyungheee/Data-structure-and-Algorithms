def solution(answers):
    answer = [0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    for i,a in enumerate(answers):
        r1 = i % len(s1)
        r2 = i % len(s2)
        r3 = i % len(s3) 
        if s1[r1] == a :
            answer[0] += 1
        if s2[r2] == a :
            answer[1] += 1
        if s3[r3] == a :
            answer[2] += 1
    result = []
    maxV = max(answer)
    for i,a in enumerate(answer) :
        if a >= maxV :
            result.append(i+1)
    result.sort()
    return result

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

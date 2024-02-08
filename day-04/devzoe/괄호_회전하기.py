def solution(s):
    answer = 0
    arr = list(s)
    a = {'[':']', '(':')', '{':'}'} 
    for i in s:
        stack = []
        for value in arr:
            if value in a.keys():
                stack.append(value)
            else :
                if len(stack) == 0 :
                    stack.append(value)
                    break
                elif a[stack[-1]] != value :
                    break
                else :
                    stack.pop()
        if len(stack) == 0 :
            answer += 1  
        p = arr[0]    
        del arr[0]
        arr.append(p)          
    return answer

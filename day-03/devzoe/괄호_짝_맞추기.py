def solution(s) :
    stack = []
    value = ['(',')']
    for a in s:
        if len(stack) == 0:
            if a == value[0] :
                stack.append(a)
                continue
            else :
                return False
        if a == value[1] :
            if stack[-1] == value[0]:
                stack.pop()
        else :
            stack.append(a)
    if len(stack) > 0 :
        return False
    return True

print(solution('(())()'))
print(solution(')'))
print(solution('((())()'))
print(solution('()()()()'))

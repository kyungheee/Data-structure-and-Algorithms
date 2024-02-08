def solution(s):
    stack = []
    for v in s:
        if len(stack) == 0:
            stack.append(v)
            continue
        elif v != stack[-1]:
            stack.append(v)
        else:
            stack.pop()
    if len(stack) == 0:
        return 1       
    return 0

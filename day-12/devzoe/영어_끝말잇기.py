def solution(n, words):
    stack = []
    for i,w in enumerate(words):
        if not stack:
            stack.append(w)
            continue
        pre = stack[-1]
        if pre[-1] != w[0] or w in stack:
            a = (i % n) + 1 
            b = (i // n) + 1
            return [a,b]
        stack.append(w)
    return [0,0]

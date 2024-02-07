def solution(dirs):
    answer = 0
    start = [0,0]
    a = []
    for d in dirs:
        s = start.copy()
        path = [s]
        if d == 'U':
            if start[1] == 5:
                continue
            start[1] += 1
        if d == 'D':
            if start[1] == -5:
                continue
            start[1] -= 1
        if d == 'L':
            if start[0] == -5:
                continue
            start[0] -= 1
        if d == 'R':
            if start[0] == 5:
                continue
            start[0] += 1
        s = start.copy()
        path.append(s)
        p = [0,0]
        p[0], p[1] = path[1], path[0]
        if path not in a and p not in a :
            a += [path]
            answer += 1
    return answer

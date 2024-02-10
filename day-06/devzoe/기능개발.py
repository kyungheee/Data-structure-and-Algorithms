from collections import deque
def solution(progresses, speeds):
    answer = []
    a = deque()
    b = deque()
    for p in progresses:
        a.append(p)
    for s in speeds:
        b.append(s)
    while a:
        for i,s in enumerate(b):
            a[i] += s         
        count = 0
        for i,v in enumerate(a):
            if v < 100 :
                break
            if v >= 100:
                count += 1
        if count != 0 :
            answer.append(count)
        for i in range(count):
            a.popleft()
            b.popleft()
    return answer

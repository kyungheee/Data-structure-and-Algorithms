def solution(N, stages):
    fail = [0 for _ in range(N)]
    for n in range(1,N+1):
        a = 0
        b = 0
        for s in stages :
            if s == n :
                a += 1
            if s >= n :
                b += 1
        if b != 0 :
            fail[n-1] = a/b
    answer = []
    while 1:
        m = max(fail)
        if m == 0 :
            break
        for i, f in enumerate(fail):
            if m == f:
                answer.append(i+1)
                fail[i] = 0
    for i in range(1,N+1):
        if i not in answer :
            answer.append(i)
    return answer

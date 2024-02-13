def solution(record):
    answer = []
    dict = {}
    for r in record:
        s = r.split()
        if len(s) == 3 :
            cmd, uid, nickname = s
            dict[uid] = nickname
            if cmd == 'Enter':
                answer += [['Enter', uid]]
        else : 
            cmd, uid = s
            answer += [['Leave', uid]]
    result = []
    for a in answer :
        if a[0] == 'Enter' :
            result += [dict[a[1]]+'님이 들어왔습니다.']
        else :
            result += [dict[a[1]]+'님이 나갔습니다.']
    return result

def solution(id_list, report, k):
    dic = {}
    for r in report :
        u, reported = r.split()
        dic[reported] = dic.get(reported, [])
        if u not in dic[reported]:
            dic[reported] = dic.get(reported, []) + [u]
    mail = {}
    for reported, users in dic.items():
        if len(users) >= k:
            for u in users:
                mail[u] = mail.get(u,0) + 1
    result = []
    for i in id_list:
        result.append(mail.get(i,0))
    return result

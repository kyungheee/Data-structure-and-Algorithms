def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}
    income = {}
    for i, e in enumerate(enroll):
        dic[e] = referral[i]
    for i, s in enumerate(seller):
        a = amount[i] * 100
        current = s
        while a > 0 and current != "-":
            ten_percent = a // 10  
            if ten_percent < 1:  
                income[current] = income.get(current, 0) + a
                break
            income[current] = income.get(current, 0) + a - ten_percent
            a = ten_percent
            current = dic.get(current, "-") 
    for e in enroll:
        answer.append(income.get(e, 0))
    return answer

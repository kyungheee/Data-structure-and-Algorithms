def solution(phone_book):
    answer = True
    dic = {}
    for p in phone_book:
        dic[p] = dic.get(p, 0) + 1
    for p in phone_book:
        for i in range(len(p)-1):
            if p[:i+1] in dic.keys():
                return False
    return True

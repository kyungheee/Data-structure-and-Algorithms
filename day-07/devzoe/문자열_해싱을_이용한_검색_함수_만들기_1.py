def solution(string_list,query_list):
    result = []
    dict = {}
    for s in string_list:
        dict[s] = 1
    for q in query_list:
        if q not in dict.keys():
            result.append(False)
        else :
            result.append(True)
    return result

print(solution(['apple','banana','cherry'],['banana','kiwi','melon','apple']))

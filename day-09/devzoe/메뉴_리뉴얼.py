from itertools import combinations
from functools import reduce
def solution(orders, course):
    answer = []
    menu = {}
    for order in orders:
        for cour in course :
            c = combinations(order,cour)
            arr = [sorted(i) for i in c]
            arr = [ reduce(lambda x, y: x + y, i) for i in arr]
            for i in arr:
                menu[i] = menu.get(i, 0) + 1
    for i, c in enumerate(course):
        a = [k for k,v in menu.items() if len(k) == c]
        a = {k : menu[k] for k in a}
        a = [k for k,v in a.items() if max(a.values()) == v and v >= 2]
        answer.extend(a)          
    return sorted(answer) 

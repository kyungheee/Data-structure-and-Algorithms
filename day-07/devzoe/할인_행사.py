def solution(want, number, discount):
    answer = 0
    a = {}
    for w, n in zip(want,number):
        a[w] = n
    for i in range(len(discount) - 9) :
        dict = {}
        for j in range(0,10):
            dict[discount[i+j]] = dict.get(discount[i+j], 0) + 1
        if all(dict.get(w, 0) >= n for w, n in a.items()):
            answer += 1
    return answer

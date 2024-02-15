# orders=["ABCFG","AC","CDE","ACDE","BCFG","ACDEH"]
# course=[2,3,4]


    from itertools import combinations
    from collections import Counter

    answer=[]

    for c in course:
        menu=[]
        for order in orders:
            comb = combinations(sorted(order),c)
            menu += comb
        # print(menu)

        counter = Counter(menu)
        # print(counter)
        # # Counter({('B', 'C', 'F', 'G'): 2, ('A', 'C', 'D', 'E'): 2,,,,,,
        # print(len(counter)) #19,20,10

        if (   len(counter) !=0    and     max(counter.values())!= 1  ):
        # counter 객체에 적어도 하나 이상의 요소가 있음을 확인
        # 그리고 최댓값이 1이 아님을 확인
        # 즉, 어떤 요소가 2회 이상 출현했을을 알 수 있다
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
                    
    return answer
    #print(answer)



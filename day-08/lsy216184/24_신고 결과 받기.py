1. (신고당한자/신고자)
2. 한사람이 동일 인물 중복 신고시 횟수는 한번으로 처리
3. 신고자의 수가 초과기준 넘는지 확인
4. (신고자/처리결과메일 횟수)


# id_list=["muzi","frodo","apeach","neo"]
# report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k=2

def solution(id_list, report, k):
    report_user = {}
    count = {}

    for i in report:
        user_id, report_id = i.split()        #신고자, 신고받은자 분리
        # print(user_id) 
        # print(report_id) 
        if report_id not in report_user:
            report_user[report_id]=set()      #중복이 없도록 초기값 설정
        report_user[report_id].add(user_id)

        #{'frodo': {'muzi', 'apeach'}, 'neo': {'muzi', 'frodo'}, 'muzi': {'apeach'}}
        #set은 유일한 요소만 저장하는 데이터 구조이며/ 데이터와 달리 순서가 없다/'set'에 요소를 추가하려면 'add'메소드를 사용해야한다 /append(x)



    for reproted_id, user_id_lst in report_user.items():
        if len(user_id_lst) >= k:
            for uid in user_id_lst:
                if uid not in count:
                    count[uid] = 1 #count에 없다면 초기값 생성
                else:
                    count[uid] +=1 #count에 있다면 +1
    # print(count)     
    #{'muzi': 2, 'apeach': 1, 'frodo': 1}       


    answer=[]
    for i in range(len(id_list)):#0,1,2,3
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    return answer

    #print(answer)

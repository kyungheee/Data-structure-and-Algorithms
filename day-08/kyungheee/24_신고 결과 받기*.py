'''
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.
'''

def solution(id_list, report, k):
    reported_user = { } # 신고당한 유저 - 신고 유저 집합을 저장할 딕셔너리
    count = { } # 처리 결과 메일을 받은 유저 - 받은 횟수를 저장할 딕셔너리

    # 신고 기록 순휘
    for r in report:
        user_id, reported_id = r.split( )
        if reported_id not in reported_user: # 신고당한 기록이 없다면
            reported_user[reported_id] = set()
        reported_user[reported_id].add(user_id) # 신고한 사람의 아이디를 집합에 담아 딕셔너리에 연결

    for reported_id, user_id_lst in reported_user.items():
        if len(user_id_lst) >= k: # 정지 기준에 만족하는지 확인
            for uid in user_id_lst: # 딕셔너리를 순회하면서 count계산
                if uid not in count:
                    count[uid] = 1
                else:
                    count[uid] += 1
    
    answer = [ ]
    for i in range(len(id_list)): # 각 아이디별 메일을 받은 횟수를 순서대로 정리
        if id_list[i] not in count:
            answer.append(0)
        else:
            answer.append(count[id_list[i]])
    
    return answer



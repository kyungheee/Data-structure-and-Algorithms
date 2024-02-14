# genres=["classic","pop","classic","classic","pop"]
# plays=[500,600,150,800,2500]

def solution(genres, plays):
    answer=[]
    genre_dict={}
    play_dict={}

    for i in range(len(genres)): #0,1,2,3,4
        genre = genres[i]
        play = plays[i]
        # print(genre)
        # print(play)

        if genre not in genre_dict:
            genre_dict[genre]=[]    #{'classic': [], 'pop': []}
            play_dict[genre]=0      #{'classic': 0, 'pop': 0}
            # print(genre_dict)
            # print(play_dict)
            # 파이썬은 키에 해당하는 값이 없는 경우 반드시 초기화 값을 명시해야 한다

        genre_dict[genre].append((i,play))
    # print(genre_dict)
    #{'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}

        play_dict[genre] += play
    # print(play_dict)
    # {'classic': 1450, 'pop': 3100}
    sorted_genre = sorted(play_dict.items(),  key = lambda x: x[1],  reverse=True)
        # .items()는 딕셔너리의 키-값 쌍을 튜플()로 된 리스트를 반환.
    #print(sorted_genre)
    #[('classic', 1450), ('pop', 3100)]
    
        # key=lambda x: x[1]는 정렬 기준을 지정하는데,
        # 여기서 x[1]은 각 튜플의 두 번째 요소, 즉 총 재생횟수를 기준으로 정렬!

        # reverse=True 정렬을 내림차순으로
        # 즉, 가장 많이 재생된 장르부터 순서대로 정렬.
        #[('pop', 3100), ('classic', 1450)]
    for genre, _ in sorted_genre:
        sorted_songs = sorted(genre_dict[genre], key=lambda x:(-x[1],x[0]))

        # sorted_genre의 [('classic', 1450), ('pop', 3100)] 중 총 재생횟수는 _로 무시한다
        # 특정 장르에 속한 리스트를 가져온다
        # -x[1]   재생횟수 높을수록 (내림차순)
        #  x[0]   인덱스 낮을수록 (오름차순) 우선순위 두고 정렬
        # print(sorted_songs)
        # [(4, 2500), (1, 600)]
        # [(3, 800), (0, 500), (2, 150)]

        answer.extend([idx for idx, _ in sorted_songs[:2]])
        # 각 장르에서 재생횟수 순으로 정렬해 최대 2곡까지 선택
    return answer
    # print(answer)

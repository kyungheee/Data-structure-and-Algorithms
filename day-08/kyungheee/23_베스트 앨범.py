'''
스트리밍 사이트에서 장르별로 가장 많이 재생된 노래를 2개씩 모아 베스트 앨범을 출시하려 합니다.

노래는 고유 번호로 구분하며, 노래 수록 기준은 다음과 같습니다.
- 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
- 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
- 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록합니다.
'''

def solution(genres, plays):
    answer = [ ]
    genres_dict ={ }
    play_dict = { }

    # 장르별 총 재생 횟수와 각 곡의 재생 횟수 저장
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genres_dict: 
            genres_dict[genre] = [] # 키에 해당하는 값이 없는 경우 반드시 초기화값을 명시해야 함
            play_dict[genre] = 0 # 얘도 초기화
        genres_dict[genre].append((i, play)) # (고유번호, 재생횟수) 튜플
        play_dict[genre] += play

    # 총 재생 횟수가 많은 장르순으로 정렬
    sorted_genres = sorted(play_dict.items(), key=lambda x: x[1], reverse= True)

    # 각 장르 내에서 노래를 재생 횟수 순으로 정렬해 최대 2곡까지 선택
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genres_dict[genre], key=lambda x : (-x[1], x[0])) # 음수를 취한 이유는 '장르 내에서 재생 횟수가 같다면 고유 번호가 낮은 노래를 먼저 수록하라'고 했기 때문
        answer.extend([idx for idx, _ in sorted_songs[:2]]) # extend() : 리스트에 다른 리스트를 추가

    return answer
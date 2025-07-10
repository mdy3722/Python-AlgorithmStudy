'''
못 푼 문제

멜론 -> 장르 별로 가장 많이 재생된 노래를 2개씩 모아 베스트 앨범을 출시,,
노래는 인덱스로 구분,,
1. 속한 노래가 많이 재생된 장르를 먼저 수록 => 장르끼리 묶어서 총 재생횟수 구함
2. 장르 내에서 많이 재생된 노래를 먼저 수록
3. 장르 내에서 재생 횟수 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록
반환 -> 노래의 인덱스를 순서대로

[풀이]
특정 키 값에 대해서 value를 모아서 합쳐주고 싶다.
특정 키 값은 아직 정해지지 않았다.
이때 dict을 사용

일단, 딩코님 코멘트 -> 많이, 많이, 많이,, 가 나오면 정렬을 써야겠구나~

[2가지 딕셔너리 필요]
dict = {"classic": 1450, "pop": 3100}
dict2 = {"classic": [(0, 500), (2, 150), (3, 800)], "pop": [(1, 600), (4, 2500)]}

sorted() 함수

sorted([1,2,3]) => 배열을 정렬함
람다 활용 -> "a"가 아닌 1처럼 뒤에 숫자를 기준으로 정렬하고 싶다. item[1]번째가 뒤에 있는 1, item[0]은 앞에꺼 (ex. "a")
sorted([("a", 1), ("b", 5), ("c", 2)], key=lambda item: item[1], reverse=True)
'''

def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]

        if genre in genre_total_play_dict:    # genre 키값이 있다면
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
        else:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)

        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break
            result.append(index)
            genre_song_count += 1

    return result
print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))
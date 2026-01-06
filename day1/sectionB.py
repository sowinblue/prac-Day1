# Section B - 리스트 선언과 접근
# B-1 : 빈 리스트 선언

music_genres = []
print(music_genres)

# B-2 : 값이 있는 리스트 선언
music_genres = ["Jazz", "Rock", "dance", "R&B"]
print(music_genres)

# B-3 : 리스트의 첫 번째 요소 접근
first_genre = music_genres[0]
print(first_genre)

# B-4 : 리스트의 마지막 요소 접근
# 음수 인덱스
last_genre = music_genres[-1]
print(last_genre)

last_genre_two = music_genres[len(music_genres) - 1]
print(len(last_genre_two))
print(last_genre_two)

# B-5 : 리스트의 길이 확인
length_genres = len(music_genres)
print(length_genres)

# B-6 : 리스트에 새 요소 추가
music_genres.append("IDM")
print(music_genres)
music_genres.append("ambient")
print(music_genres)

# B-7 : 리스트의 특정 위치 요소 변경
music_genres[1] = "Jpop"
print(music_genres)

# insert 메서드로 특정 위치에 요소 추가
music_genres.insert(1, "kpop")
print(music_genres)

# B-8 : 리스트에서 요소 제거
remove_genre = music_genres.pop(2)
print(remove_genre)
print(music_genres)

remove_genre_two = music_genres.remove("R&B")
print(remove_genre_two)
print(music_genres)

del music_genres[2]
print(music_genres)

# Section D - Create와 Read의 조합
# D-1 : 이름 하나 입력받아 리스트에 추가 후 전체 출력

genre = input("좋아하는 음악 장르를 입력 하세요")

music_genres = []
music_genres.append(genre)

print(music_genres)

# D-2 : 여러 이름 받아 리스트에 추가 후 전체 출력

genre1 = input("좋아하는 음악 장르를 입력 하세요: ")
genre2 = input("좋아하는 음악 장르를 입력 하세요: ")
genre3 = input("좋아하는 음악 장르를 입력 하세요: ")

music_genres_two = []
music_genres_two.append(genre1)
music_genres_two.append(genre2)
music_genres_two.append(genre3)

print(music_genres_two)


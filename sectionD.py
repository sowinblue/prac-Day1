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


# D-3 : 이름 입력받아 추가, 전체 개수 출력
# 변수 이름 할당해서 하는 것이 유지 보수에 좋다
gerne = input("장르를 입력: ")

gerne_three=["jazz", "dance"]
gerne_three.append(gerne)
count = len(gerne_three)
print(count)


# D-4 : 반복문으로 여러 이름 입력받아 리스트 구성
genres_four=[]
counts= range(3)
for i in counts:
    genre = input("장르를 입력해!!: ")
    genres_four.append(genre)

print(genres_four)


# D-5 : 리스트에서 특정 이름 검색
genre = input("장르 조회: ")

if genre in genres_four:
    print(genre)
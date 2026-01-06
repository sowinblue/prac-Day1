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


# D-6: 리스트에서 특정 인덱스 요소 출력
target = gerne_three[1]
print(target)

# D-7 : 입력받은 인덱스로 요소 접근
# 내가 푼 방법
idx=int(input("숫자를 입력하시오: "))
print(gerne_three[idx])

# 유지 보수 좋은 코드
idx=int(input("숫자를 입력하시오: "))
target1 = gerne_three[idx]
print(target1)

# D-8 : 전체 목록 번호와 함께 출력
gerne_list = ["jazz","hiphop","band","dance"]

for idx,ger_name in enumerate(gerne_list):
    print(idx,ger_name)
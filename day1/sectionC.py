# Section C - for문 기초
# C-1 : 리스트 전체 순회 출력
music_genres = ["Jazz", "Rock", "dance", "R&B"]


for genre in music_genres:
    print(genre)

for i,genre in enumerate(music_genres):
    print(i, genre)

# C-2 : range로 숫자 순회
# 같은 범위를 여러 곳에서 사용하거나 나중에 쉽게 바꾸고 싶다면 → 첫 번째 방식(변수에 할당) 추천
# 유지보수가 좋은 코드

numbers = range(3)
for num in numbers:
    print(num)


# 짧고 한 번만 사용하는 경우 → 두 번째 방식(직접 range 넣기) 추천
for number in range(3):
    print(number)


# C-3 :enumerate로 인덱스와 함께 순회
# 인덱스 값과 요소 값이 함께 필요한 상황 -> 각 변수에 따로 할당
for i,genre in enumerate(music_genres):
    print(i, genre)

# (인덱스,값)튜플 형태로 반환
for full in enumerate(music_genres):
    print(full)


# C-4 : 순회하며 특정 요소만 충족
# 요소 안에 포함 되어 있는 것을 찾을 때: if - in 키워드 사용
for genre in music_genres:
    if "a" in genre:
        print(genre)

# 요소가 특정 값과 같은지 찾을 때: if - == 키워드 사용
for genre in music_genres:
    if genre == "R&B":
        print(genre)

# 추가 활용
user_genre = input("장르를 입력하세요: ")

if user_genre in music_genres:
        print(user_genre)
else:
        print(f"해당 {user_genre} 장르는 없습니다.")


# C-5 : 순회하며 새 리스트에 추가
music_genres = ["Jazz", "Rock", "dance", "R&B"]
new_music_genres = []
for genre in music_genres:
    new_music_genres.append(genre)

print(new_music_genres)

# 응용: 특정 조건을 만족하는 요소만 새 리스트에 추가
a_in_genres = []
for genre in music_genres:
    if "a" in genre:
        a_in_genres.append(genre)

print(a_in_genres)

# C-6 : 순회하며 값 누적
member_age = [23, 29, 31, 35, 40]
total = 0

for num in member_age:
    total += num

print(total)
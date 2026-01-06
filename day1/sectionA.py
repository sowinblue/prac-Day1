#section A - 변수 선언과 할당
# A-1 : 문자열 변수 하나 선언
name = "블루윈"
print(name)


# A-2 : 숫자 변수 하나 선언
age = 25
print(age)


# A-3 : 문자열 변수 두 개 선언 후 연결
first_name= "블루"
last_name = "윈"
full_name = first_name + last_name
print(full_name)



# A-4 : 숫자 변수 두 개 선언 후 연산
num1 = 210
num2 = 912
sum_result = num1 + num2
print(sum_result)


age = 25
next_year_age = age + 1
print(next_year_age)



#* 오류: 문자열에는 값을 할당 할 수 없음( 리터럴에 변수 할당 불가)
# "A4hz" = 440
# "A5hz" = "A4hz" * 2
# print("A5hz")


# "A4hz"를 변수로 사용하고 싶다면 딕셔너리를 이용해서 사용
notes = {}
notes["A4hz"] = 440
notes["A5hz"] = notes["A4hz"] * 2
print(notes["A5hz"])  # 880
print(notes)


A4hz = 440
A5hz = A4hz * 2
print(A5hz)



# A-5 : 변수에 새 값 재할당
# 재할당 하면 기존값은 더 이상 참조되지 않음
# 변수는 동적 타이핑 -> 값의 타입이 달라도 같은 이름으로 재할당 가능
# python만의 특징이 아닌 대부분의 프로그래밍 언어에서 변수 재할당(Reassignment)이 허용되는 일반적인 동작
nickname = "블루윈"
nickname = "그린윈"
print(nickname)


# A-6 : 변수 값을 다른 변수에 할당
original = "파란색"
copy = original
print(copy)


# A-7 : 입력 받은 값을 변수에 할당
# A-8 : 입력받은 두 값을 각각 변수에 저장
name = input("이름을 입력하세요: ")
place = input("가고 싶은 곳을 입력하세요: ")
print(f"안녕하세요! {name}님 {place}에 가고 싶으시군요! 화이팅하세요!")
print(name)
print(place)

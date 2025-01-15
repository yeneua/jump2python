## 문자열 자료형
a = 'Python\'s favorite food is perl' # 역슬래시로 작은 따옴표 출력
print('문자열 자료형 작은 따옴표 출력', a)

b = "\"Hello World\""
print('문자열 자료형 큰 따옴표 출력', b)


## 여러 줄인 문자열 변수에 대입
multiline1 = "Life is too short\nYou need python" # 1. 이스케이프 문자
multiline2 = '''Life is too short 
you need python''' # 따옴표 3개
multiline3 = """Life is too short
you need python"""


## 이스케이프 문자
print("이스케이프 문자 개\n행 탭\t간격 슬\\래시 사용 작은\'따옴표 큰\"따옴표")


## 문자열 연결
head = 'python'
tail = ' is fun'
print('문자열 연결', head + tail)


## 문자열 곱하기
a = 'python'
print('문자열 곱하기', a*2) # pythonpython : 2번 반복하라는 뜻

print("="*50, "\n문자열 곱하기 응용 Program\n", "="*50)


## 문자열 길이 구하기
print("문자열 길이(공백 포함합니당)", len("Life is too short"))


## 문자열 인덱싱
a = "Life is too short"
print(a[3]) # e
print(a[0]) # L
print(a[-0]) # L
print(a[-1]) # t
print(a[-2]) # r
print(a[-7]) # o


## 문자열 슬라이싱 - 여러개 뽑기
a = "Life is too short"
# Life is too   s h o r t
# 012345678910111213141516
#       -9-8-7-6-5-4-3-2-1     
print(a[0:4]) # 인덱스 0~3까지 0 <= a < 3
print(a[7:]) # 7~끝까지
print(a[:10]) # 처음부터~9까지
print(a[:]) # 처음부터 끝까지
print(a[8:-7]) # 인덱스 8~-6까지(-7포함x)


## 문자열은 '변경 불가능한(immutable) 자료형'
a = 'Pithon'
# a[1] = 'y'
# print(a) # Error


## 문자열 포매팅
print("문자열 포매팅", "I eat %d apples" %3)
print("I eat %s bananas" %"five")

num = 3
print("I eat %d grapes" %num)

num = 10
day = 'three'
print("문자열 포매팅 2개 이상 값 넣기", "I ate %d apples, I was sick for %s days" %(num, day))

print("I eat %s apples" %3) # %s는 어떤 형태 값이든 문자열로 변환해서 넣음
# %c 는 문자열 1개를 나타낼 때 사용

# 퍼센트(%) 기호
print("Error is %d%%" %98) # %% 두개 같이 사용


## 포맷 코드 + 숫자 함께 사용
print("%10s" %"hi") #________hi (공백 8칸+hi: 오른쪽정렬 출력됨)
print("%-10s" %"hi") #hi________ (hi+공백 8칸 : 왼쪽정렬)


## 소수점 표현
print("%0.4f" %3.14159265) # 소수점 네번째 자리까지 표현
print("%.4f" %3.14159265) # 위와 같은 표현

print("%10.4f" %3.14159265) #____3.1415 (공백4칸+3.1415 : 총 10칸)


## format 함수 사용 포매팅
print("\"format 함수 사용 포매팅\"", "I eat {0} apples".format(3))
print("I ate {0} bananas".format("five"))
num = 3
print("I ate {0} apples".format(num))

print("I eat {0} apples, I was sick for {1} days".format(10, 3)) # {0}, {1}이 인덱스임 -> 각각 10, 3을 가리킴

print("I eat {num} apples, I was sick for {day} days".format(num=5, day=5)) # 이름으로 넣기

print("I ate {0} grapes, so I was sick {days} days".format(10, days=6)) # 인덱스 + 이름 혼용 가능


## 왼쪽 정렬
print("{0:<10}".format("hi"))


## 오른쪽 정렬
print("{0:>10}".format('hi'))


## 가운데 정렬
print("{0:^10}".format('hi'))


## 공백 채우기
print("{0:=^10}".format('hi'))
print("{0:=<10}".format('hi'))


## 소수점 채우기
print("%0.4f" %3.141592) # %0.4f : 소수점 넷째 자리까지 표기
print("{0:0.4f}".format(3.141592))
print("{0:10.4f}".format(3.141592))


## 중괄호 표시하기
print("{{ and }}".format())


## f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age+1}입니다.')

dic = {'name' : "홍길동", 'age' : 30}
print(f'나의 이름은 {dic["name"]}이고, 나이는 {dic['age']}입니다.')


## 문자열 관련 함수
a = 'text'
print(a.count('t')) # 문자 개수 세기 count

print(a.find('x')) # 위치 알려주기 find
print(a.find('k')) # 없는 문자일 경우 -1 반환

print(a.index('e'))
# print(a.index('k')) # 없는 문자일 경우 에러 반환

print(",".join('abcd')) # 문자열 삽입 join
print(",".join(['a','b','c','d']))

print("hi".upper()) # 소문자 -> 대문자 upper. a 자체의 문자열이 바뀌는 것x. 그저 결과를 출력해줄뿐. a=a.upper() 해야 바뀜
print("HI".lower()) # 대문자 -> 소문자 lower

print(" hi ".lstrip()) # 왼쪽 공백 지우기 lstrip
print(" hi ".rstrip()) # 오른쪽 공백 지우기 rstrip
print(" hi ".strip()) # 양쪽 공백 지우기 strip

print("Life is too short".replace("Life","your leg")) # 문자열 바꾸기 replace


print("Life is too short".split()) # 문자열 나누기 split
print("a:b:c:d".split(":")) # 리스트로 반환됨
# 숫자형 자료형

# 1. 정수형(int)
a = 123
print(type(a)) # <class 'int'>
a = -178
a = 0

# 2. 실수형(float)
a = 1.2
a = -3.45
print(type(a)) # <class 'float'>
b = 4.24E10 # 42400000000.0(4.24*10^10)

# 3. 8진수, 16진수
a = 0o10
print(a) # 8(10진수로 출력됨)

a = 0xb
print(a) # 11


# 사칙 연산
a, b= 5, 2
print(a + b)
print(a - b)
print(a*b)
print(a/b)
print(a**b) # 제곱
print(a//b) # 몫
print(a%b) # 나머지
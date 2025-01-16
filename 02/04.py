## 튜플 자료형
# 1. 소괄호(생략 가능)
# 2. 요소가 한 개일 경우 요소 뒤에 쉼표
# 3. 값 수정 불가

t1 = (1,2,3)
t2 = (1,)
t3 = (1, 2, 3)
t4 = ()
t5 = ('a','b',('ab','cd'))


## 값 삭제
t1 = (1,2,'a','b')
# del t1[0] # TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 'c '# TypeError: 'tuple' object does not support item assignment


## 튜플 더하기
t1 = (1,2,'a','b')
t2 = (3,4)
t3 = t1+t2
print(t3) # (1,2,'a','b',3,4)


## 튜플 곱하기
t1 = (3,4)
t2 = t1 * 3
print(t2) # (3,4,3,4,3,4,)

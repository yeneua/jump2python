## 리스트 자료형

a = list() # 비어있는 리스트 생성

a = [1, 2, 3, ['a','b','c']]
print(a[-1]) # ['a','b','c']
print(a[3][2]) # c


## 리스트 더하기
a = [1,2,3]
b = [4,5,6]
print(a+b) # [1,2,3,4,5,6]


## 리스트 반복하기
a = [1,2,3]
print(a*3) #[1,2,3,1,2,3,1,2,3]


## 값 수정
a = [1,2,3]
a[2] = 4
print(a) # [1,2,4]


# 요소 삭제하기 delete
a = [1,2,3]
del a[1] # 인덱스 1을 삭제함
print(a)

b = [4,5,6]
del b[1:]
print(b) # [4]


## 요소 추가하기 append
a = [1,2,3]
a.append(4) # 젤 뒤에 추가됨
print(a)
a.append([5,6])
print(a) # [1,2,3,4,[5,6]]


## 리스트 정렬 sort
a = [2,4,3,1]
a.sort() # 오름차순 정렬
print(a)
b = ['a','c','b',"A"]
b.sort()
print(b) #['A','a','b','c']


## 리스트 뒤집기 reverse
a = ['a','c','b']
a.reverse()
print(a) #['b','c','a']


## 인덱스 반환 index
c = [1,2,3]
print(c.index(3)) # 3값의 인덱스(위치) 값을 리턴 => 2
print(c.index(1)) # => 0
# print(c.index(0)) # => 에러(존재하지 않는 값)


## 요소 삽입 insert
a = [1,2,3]
a.insert(0,4) # insert(a, b) : a번째 위치에 b를 삽입 => 인덱스 0에 4를 삽입
print(a)
a.insert(3,[5,6])
print(a)


## 리스트 요소 제거 remove
a = [1,2,3,1,2,3]
a.remove(3) # remove(x) : 첫번째로 나오는 x값을 제거함
print(a) # [1,2,1,2,3]
a.remove(3)
print(a) # [1,2,1,2]


# 리스트 요소 끄집어 내기 pop
a = [1,2,3]
a.pop() # 3을 끄집어 냄
print(a) # => [1,2]

a.pop(1) # a[1]을 끄집어 냄
print(a) # => [1]


## 개수 세기 count
a = [1,2,3,1]
print(a.count(1)) # 1이 몇갠지 셈 => 2


## 리스트 확장 extend
# extend(x) : x에는 리스트만 올 수 있음
a = [1,2,3]
a.extend([4,5])
print(a) # [1,2,3,4,5]

b = [6,7]
a.extend(b)
print(a) # [1,2,3,4,5,6,7]

a+=[9,10]
print(a) #[1,2,3,4,5,6,7,9,10]
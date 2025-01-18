## 딕셔너리 자료형
# key와 value가 한 쌍
# 순차적 x


## 딕셔너리 생성
dic = {'name':'KIM', 'phone' : '010-1111-2222', 'birth' : '1117'}

a = {1 : 'hi'}

a = {'a': [1,2,3]} # 리스트도 넣을 수 있음


## 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b' # key가 2이고, value가 'b'인 쌍이 추가됨
print(a) # {1:'a',2:'b'}

a['name'] = 'pey'
print(a) #{1:'a', 2:'b', 'name' : 'pey'}

a['e'] = [1,2,3]
print(a) # {1:'a', 2:'b', 'name':'pey', 'e' :[1,2,3]}


## 딕셔너리 요소 삭제하기
del a[1] # del 딕셔너리이름[key] => 1이라는 key에 해당하는 쌍이 삭제됨
print('딕셔너리 삭제하기',a)


## 딕셔너리 사용 방법
grade ={'hong' : 10, 'julliet' : 99}
print(grade['hong']) # key의 value를 얻는 방법
print(grade['julliet'])

dic = {'name' : 'Hong', 'phone' : '010-1111-2222', 'birth' : '1117'}
print(dic['name'])
print(dic['birth'])
print(dic['phone'])


## 딕셔너리 만들때 주의 사항 - key는 고유한 값!!! 중복 존재 불가
a = {1:'a', 1 : 'b'}
print(a[1]) # => b 만 출력됨 1:'a' 쌍은 무시된다.


## key 값은 변하지 않는(immutable) 값만 가능 : 튜플 가능, 리스트 불가
# a = {[1,2] : 'hi'} # TypeError: unhashable type: 'list'
a = {(1,) : 'hi'}
print(a[(1,)])


## key 리스트 만들기 : keys()
a = {'name' : 'Hong', 'birth' : '1117', 'phone' : '010-1111-2222'}
print(a.keys()) # => dict_keys(['name', 'birth', 'phone']) : dict_keys라는 객체로 리턴함
print(list(a.keys())) # 리스트로 리턴하고 싶을 경우
print(type(list(a.keys()))) # <class 'list'>

# dict_keys 객체 -> 기본 반복 구문(for)에서는 사용 가능. but, append, inseret, pop, remove, sort 불가(리스트가 아니니까!)
for k in a.keys():
    print('dict_keys 객체',k)

print(a.values()) # dict_values(['Hong', '1117', '010-1111-2222']) : dict_values 라는 객체로 리턴함
print(list(a.values())) # ['Hong', '1117', '010-1111-2222']

print(a.items()) # dict_items([('name', 'Hong'), ('birth', '1117'), ('phone', '010-1111-2222')]) : key와 values의 쌍을 튜플로 묶은 값을 dict_itmes 객체로 리턴
c = list(a.items())
print(c) # [('name', 'Hone'), ('birth', '1117'), ('phone', '010-1111-2222')]
print(type(c)) # 리스트
print(type(c[0]), c[0]) # 튜플 ('name', 'Hong')
print(c[0][0]) # name


## key : value 쌍 모두 지우기
a.clear()
print(a) # {} : 빈 딕셔너리


## get() : key로 value 얻기
a = {'name' : 'Hong', 'birth' : '1117', 'phone' : '010-1111-2222'}
print(a.get('name')) # Hong
print(a.get('phone')) # 010-1111-2222

# 없는 key로 값을 가져오려고 할때
print(a.get('notfound')) # None
# print(a['notfound']) # KeyError: 'notfound'

print(a.get('notfound','default')) # get(x,'디폴트 값') : 존재하지 않는 key일 경우 디폴트 값을 대신 가져오게 함


## in : 해당 key가 있는지 조사하기 - True/False 값 리턴
a = {'name' : 'Hong', 'birth' : '1117', 'phone' : '010-1111-2222'}
print('name' in a) # => True
print('foo' in a) # => False
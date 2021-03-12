Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> exist=True
>>> exist
True
>>> type(exist)
<class 'bool'>
>>> pi=3.14
>>> r=2
>>> print(pi*r**2)
12.56
>>> a=3
>>> b=3.5
>>> print(a+b)
6.5
>>> print(a-b)
-0.5
>>> print(a*b)
10.5
>>> print(a/b)
0.8571428571428571
>>> print(a%b)
3.0
>>> two = 0b11
>>> print(two)
3
>>> #2진수는 0b를 사용
>>> eight=0o11
>>> print(eight)
9
>>> #8진수는 0o를 사용
>>> a=0x11
>>> print(a)
17
>>> #16진수는 0x를 사용
>>> 
>>> #다수의 데이터 형 출력
>>> name='blake'
>>> print('im', name)
im blake
>>> print(1,2,3)
1 2 3
>>> #정수형 값 3rofmf cnffur
>>> print('1','2','3')
1 2 3
>>> #문자열형 값 3개를 출력
>>> a=5
>>> b=3
>>> print(a, '//', b, '=', a//b)
5 // 3 = 1
>>> print(a, '%', b, '=', a%b)
5 % 3 = 2
>>> a=5
>>> b=a
>>> b= b-2
>>> print('a=', a, 'b=' , b)
a= 5 b= 3
>>> 
>>> #C언어와 유사 형태 출력방식
>>> print("%d"% 3)
3
>>>  print("%f"% 3.5)
 
SyntaxError: unexpected indent
>>> print("%f"% 3.5)
3.500000
>>> #입력함수
>>> #input()
>>> name=input()
최혜지
>>> print(name)
최혜지
>>> name=input('이름:')
이름:blake
>>> print(name)
blake
>>> age=input('age:')
age:30
>>> print(age)
30
>>> after=input('after few years:')
after few years:3
>>> print(age+after)
303
>>> #input()함수로 입력된 모든 값들은 문자열로 저장
>>> print(int(age)+int(after))
33
>>> print(int('10')+21)
31
>>> a=input('변수a:')
변수a:3
>>> b=input('변수b:')
변수b:5
>>> print(a+b)
35
>>> print(int(a)+int(b)
      )
8
>>> 
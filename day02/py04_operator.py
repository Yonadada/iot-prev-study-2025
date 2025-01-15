# 연산자

#덧셈
a = 10
b = 23
c = a + b
print(c)

#뺄셈
c = a - b
print(c)

#곱셈
c = b * a  # -> 곱셈연산에는 x(영문자, 특수문자) 사용안한다. * 을 사용
print(c)    

#나눗셈
c = b / a  # 나눈 결과가 실수 
print(c) 

c = b // a # 나눈 결과가 정수(몫)
print(c) 

c = b % a  # 나눈 결과의 나머지
print(c) 

c = a ** 3 # 승수계산
print(c)


c = b / 0 # 예외 발생! -> 예외처리를 해야함
print(c)

